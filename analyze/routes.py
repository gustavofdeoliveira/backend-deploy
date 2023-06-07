from sanic.response import HTTPResponse,json
from middleware.body_check import validate_body
from analyze.utils import Schema
from analyze.controller import register, get_all, get_analyze, update_analyze, delete_analyze
from sanic import Blueprint, Websocket, Request
from ultralytics import YOLO
import numpy as np
import cv2 as cv
import asyncio
from sanic_ext import openapi
from analyze.service import AnalyzeTestCreate, AnalyzeTestUpdate
import os
import boto3
from botocore.exceptions import ClientError
import cv2
from datetime import datetime

analyze = Blueprint('analyze', __name__)

model = YOLO('analyze/best.pt')
clients = []
frame_queue = asyncio.Queue()


@analyze.post("/create")
@openapi.summary("Create a new analyze")
@openapi.description("This endpoint allows you to create a new analyze.")
@openapi.definition(body={'application/json': AnalyzeTestCreate.schema()},)
# @validate_body(Schema.REGISTER.value)
async def handler_register(request: Request) -> HTTPResponse:
    data = request.json
    response, code = register(routeId=data['routeId'], name=data['name'], startDate=data['startDate'], endDate=data['endDate'], supervisor=data['supervisor'], operator=data['operator'])
    return json(response, code)


@analyze.get("/get_analyzes")
@openapi.summary("Get all analyzes")
@openapi.description("This endpoint allows you to get all analyzes. And you don't need to send any data.")
async def handler_get_all(request: Request) -> HTTPResponse:
    response, code = get_all()
    return json(response, code)


@analyze.get("/get_analyze/<id:int>")
@openapi.summary("Get a analyze")
@openapi.description("This endpoint allows you to get a analyze.")
async def handler_get_analyze(request: Request, id: int) -> HTTPResponse:
    response, code = get_analyze(id=id)
    return json(response, code)

@analyze.put("/update_analyze")
@openapi.summary("Update a analyze")
@openapi.description("This endpoint allows you to update a analyze. And you need to send all data.")
@openapi.definition(body={'application/json': AnalyzeTestUpdate.schema()},)
#@validate_body(Schema.UPDATE.value)
async def handler_update_analyze(request: Request) -> HTTPResponse:
    data = request.json
    response, code = update_analyze(id=data['id'], routeId=data['routeId'], name=data['name'], startDate=data['startDate'], endDate=data['endDate'], supervisor=data['supervisor'], operator=data['operator'], createdAt=data['createdAt'])
    return json(response, code)

@analyze.delete("/delete_analyze/<id:int>")
@openapi.summary("Delete a analyze")
@openapi.description("This endpoint allows you to delete a analyze.")
#@validate_body(Schema.DELETE.value)
async def handler_delete_analyze(request: Request, id: int) -> HTTPResponse:
    response, code = delete_analyze(id)
    return json(response, code)

@analyze.post("/video_upload")
@openapi.summary("Upload a video from camera")
@openapi.description("This endpoint allows you to upload a video from camera.")
async def video_upload(request: Request) -> json:
    print(len(request.files.get('image')))
    print(type(request.files.get('image')))
    image_bytes = request.files.get('image')[1]
    nparr = np.fromstring(image_bytes, np.uint8)
    img = cv.imdecode(nparr, cv.IMREAD_COLOR)
    result = model.predict(img, conf=0.4)
    output_image = result[0].plot()
    image_name = 'analyze-image-'+ str(datetime.now().strftime("%m-%d-%Y-%H-%M-%S"))+'.jpg'
    cv2.imwrite('analyze/images/'+ image_name, output_image)
    
    images = []

    
    s3 = boto3.resource('s3')
    with open('analyze/images/'+image_name, 'rb') as data:
        s3.Bucket('bucket-analyze-images').put_object(Key=image_name, Body=data)   
        images.append('https://bucket-analyze-images.s3.amazonaws.com/'+image_name)
    os.remove('analyze/images/'+image_name)

    await frame_queue.put(result[0].plot())

    return json({"status": "success"})

@analyze.websocket("/video_feed")
@openapi.summary("Get image from camera")
@openapi.description("This endpoint allows you to get image from camera.")
async def video_feed(request: Request, ws: Websocket):
    clients.append(ws)
    try:
        while True:
            frame = await frame_queue.get()
            if frame is not None:
                _, buffer = cv.imencode('.jpg', frame)
                frame_bytes = buffer.tobytes()

                tasks = []
                for client in clients:
                    tasks.append(asyncio.create_task(client.send(frame_bytes)))
    
                await asyncio.gather(*tasks)
    except Exception as err:
        print(err)
    finally:
        clients.remove(ws)
