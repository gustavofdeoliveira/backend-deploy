from sanic.request import Request
from sanic import Blueprint
from sanic.response import HTTPResponse, json
from sanic_ext import cors
from middleware.body_check import validate_body
from robot.utils import Schema
from robot.controller import register, get_robots, get_robot, delete_robot
from sanic_ext import openapi
from robot.service import RobotTestCreate

robot = Blueprint('robot', __name__)


@robot.post("/create")
@openapi.summary("Create a new robot")
@openapi.description("This endpoint allows you to create a new analyze.")
@openapi.definition(body={'application/json': RobotTestCreate.schema()})
@validate_body(Schema.REGISTER.value)
async def handler_register(request: Request) -> HTTPResponse:
    data = request.json
    response, code = register(
        name=data['name'],
        ip=data['ip'])
    return json(response, code)


@robot.get("/get_robots")
@openapi.summary("Get all robots")
@openapi.description("This endpoint allows you to get all robots. And you need to send the id")
async def handler_get_robots(request: Request) -> HTTPResponse:
    response, code = get_robots()
    return json(response, code)


@robot.get("/get_robot/<id:int>")
@openapi.summary("Get a robot")
@openapi.description("This endpoint allows you to get a robot. And you need to send the id")
async def handler_get_robot(request: Request, id) -> HTTPResponse:
    response, code = get_robot(id)
    return json(response, code)


@robot.delete("/delete_robot/<id:int>")
@openapi.summary("Delete a robot")
@openapi.description("This endpoint allows you to delete a robot. And you need to send the id")
async def handler_delete_robot(request: Request, id) -> HTTPResponse:
    response, code = delete_robot(id)
    return json(response, code)
