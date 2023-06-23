import asyncio

import cv2 as cv
from sanic import Blueprint, Websocket, Request
from sanic.response import HTTPResponse, json
from sanic_ext import openapi
from ultralytics import YOLO

from analyze.controller import register, get_all, get_analyze, update_analyze, delete_analyze, receive_image, \
    create_sensor_data
from analyze.service import AnalyzeTestCreate, AnalyzeTestUpdate

analyze = Blueprint('analyze', __name__)

model = YOLO('analyze/best.pt')
clients = []
frame_queue = asyncio.Queue()


@analyze.post("/create")
@openapi.summary("Create a new analyze")
@openapi.description("This endpoint allows you to create a new analyze.")
@openapi.definition(body={'application/json': AnalyzeTestCreate.schema()}, )
# @validate_body(Schema.REGISTER.value)
async def handler_register(request: Request) -> HTTPResponse:
    data = request.json
    response, code = register(
        routeId=data['routeId'], 
        name=data['name'], 
        status='In progress',
        startDate=data['startDate'],
        endDate=data['endDate'], 
        supervisor=data['supervisor'], 
        operator=data['operator'],
        robotId=int(data['robotId']))
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
@openapi.definition(body={'application/json': AnalyzeTestUpdate.schema()}, )
# @validate_body(Schema.UPDATE.value)
async def handler_update_analyze(request: Request) -> HTTPResponse:
    data = request.json
    response, code = update_analyze(
        id=data['id'], 
        routeId=data['routeId'], 
        name=data['name'], 
        status=data['status'],
        startDate=data['startDate'], 
        endDate=data['endDate'], 
        supervisor=data['supervisor'],
        operator=data['operator'])
    return json(response, code)


@analyze.delete("/delete_analyze/<id:int>")
@openapi.summary("Delete a analyze")
@openapi.description("This endpoint allows you to delete a analyze.")
# @validate_body(Schema.DELETE.value)
async def handler_delete_analyze(request: Request, id: int) -> HTTPResponse:
    response, code = delete_analyze(id)
    return json(response, code)


@analyze.post("/video_upload/<id:int>")
@openapi.summary("Upload a video from camera")
@openapi.description("This endpoint allows you to upload a video from camera.")
async def video_upload(request: Request, id: int) -> json:
    try:
        image_bytes: bytes = request.files.get('image')[1]
        response, code = receive_image(image_bytes, id)
        return json(response, code)
    except Exception as err:
        return json({'message': 'Error, image not sent due to this error: {err}'}, 500)


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
            else:
                break
    except Exception as err:
        print(err)
    finally:
        clients.remove(ws)
        return json({'message': 'No video available'}, 200)


VALORES_RECEBIDOS = []


@analyze.websocket("/gas-sensor/<id:int>")
async def gas_sensor(request: Request, ws: Websocket, id: int):
    while True:
        try:
            data = await ws.recv()
            if isinstance(data, str) and data.isdigit() and int(data) > 0:
                VALORES_RECEBIDOS.insert(0, int(data))
                print(f'CHEGOU O VALOR! ---> {data}')
                response, code = create_sensor_data(id, int(data))
            if response:
                await ws.send(f"{response['message']} with code {code}")
            else:
                await ws.send(f"Data is not valid!")
        except Exception as err:
            print(f"ERROOORR!! {err}")


@analyze.websocket("/gas-sensor-frontend")
async def gas_sensor_reading(request: Request, ws: Websocket):
    while True:
        try:
            if VALORES_RECEBIDOS:
                await ws.send(str(VALORES_RECEBIDOS.pop()))
            else:
                await asyncio.sleep(0.5)
        except Exception as err:
            print(f"ERROOORR!! {err}")
            await asyncio.sleep(1)
