from sanic.request import Request
from sanic import Blueprint
from sanic.response import HTTPResponse,json
from sanic.response import json
from textwrap import dedent
from middleware.body_check import validate_body
from route.utils import Schema
from route.controller import register, get_all, get_route, update_route, delete_route
from sanic_ext import openapi
from route.service import RouteTestCreate, RouteTestUpdate

route = Blueprint('route', __name__)

@route.post("/create")
@openapi.summary("Create a new route")
@openapi.description("This is endpoint allows you to create a new route.")
@openapi.definition(body={'application/json': RouteTestCreate.schema()})
@validate_body(Schema.REGISTER.value)
async def handler_register(request: Request) -> HTTPResponse:
      data = request.json
      response, code = register(name=data['name'])
      return json(response, code)

@route.get("/get_all")
@openapi.summary("Get all routes")
@openapi.description("This is endpoint allows you to get all routes.")
async def handler_get_all(request: Request) -> HTTPResponse:
      response, code = get_all()
      return json(response, code)

@route.get("/get_route/<id:int>")
@openapi.summary("Get a route")
@openapi.description("This is endpoint allows you to get a route.")
#@validate_body(Schema.GET.value)

async def handler_get(request: Request, id: int) -> HTTPResponse:
      response, code = get_route(id)
      return json(response, code)

@route.put("/update_route")
@openapi.summary("Update a route")
@openapi.description("This is endpoint allows you to update a route.")
@openapi.definition(body={'application/json': RouteTestUpdate.schema()})
@validate_body(Schema.UPDATE.value)
async def handler_update(request: Request) -> HTTPResponse:
      data = request.json
      response, code = update_route(id=data['id'], name=data['name'], createdAt=data['createdAt'])
      return json(response, code)

@route.delete("/delete_route/<id:int>")
@openapi.summary("Delete a route")
@openapi.description("This is endpoint allows you to delete a route.")
#@validate_body(Schema.DELETE.value)
async def handler_delete(request: Request, id: int) -> HTTPResponse:
      response, code = delete_route(id)
      return json(response, code)
