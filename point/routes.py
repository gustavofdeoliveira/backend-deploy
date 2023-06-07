
from sanic.request import Request
from sanic import Blueprint
from sanic.response import HTTPResponse,json
from middleware.body_check import validate_body
from point.utils import Schema
from sanic_ext import openapi
from point.controller import register, get_points, delete_points
from point.service import PointTestCreate

point = Blueprint('point', __name__)

@point.post("/create")
@openapi.summary("Create a point")
@openapi.description("This endpoint allows you to get register a point. And you need to send pointX, pointY, routeId")
@openapi.definition(body={'application/json': PointTestCreate.schema()},)
#@validate_body(Schema.REGISTER.value)
async def handler_register(request: Request) -> HTTPResponse:
      data = request.json
      response, code = register(pointX=data['pointX'], pointY=data['pointY'], routeId=data['routeId'])
      return json(response, code)

@point.get("/get_points/<routeId:int>")
@openapi.summary("Get all points of a route")
@openapi.description("This endpoint allows you to get all points of a route. And you need to send routeId")
#@validate_body(Schema.GET_POINTS.value)
async def handler_get_points(request: Request, routeId) -> HTTPResponse:
        response, code = get_points(routeId)
        return json(response, code)

@point.delete("/delete_points/<routeId:int>")
@openapi.summary("Delete all points of a route")
@openapi.description("This endpoint allows you to delete all points of a route. And you need to send routeId")
#@validate_body(Schema.DELETE_POINTS.value)
async def handler_delete_points(request: Request,routeId) -> HTTPResponse:
        response, code = delete_points(routeId)
        return json(response, code)
