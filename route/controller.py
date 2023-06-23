from route.service import Route
from datetime import datetime

# This function registers a route with the provided details and returns a message.
def register(name:str) -> tuple[dict[str, str], int]:
    try:
        route = Route(name=name)
        message = route.register()
        return {'message': message}, 200
    except Exception as e:
        return {'error': str(e)}, 500

# This function gets all the routes in the database and returns a list of routes.
def get_all() -> tuple[list[dict[str, str]], int]:
    try:
        routes = Route()
        routes = routes.get_all()
        return {'routes':routes}, 200
    except Exception as e:
        return {'error': str(e)}, 500

# This function gets a route with the provided id and returns a route.
def get_route(id: int) -> tuple[dict[str, str], int]:
    try:
        route = Route()
        route = route.get_route(id)
        return {'route':route}, 200
    except Exception as e:
        return {'error': str(e)}, 500

# This function updates a route with the provided details and returns a message.  
def update_route(id: int, name: str, createdAt: datetime) -> tuple[dict[str, str], int]:
    try:
        route = Route(id=id, name=name, createdAt=createdAt)
        message = route.update_route()
        return {'message': message}, 200
    except Exception as e:
        return {'error': str(e)}, 500

# This function deletes the route with the provided id and returns a message.  
def delete_route(id: int) -> tuple[dict[str, str], int]:
    try:
        route = Route()
        message = route.delete_route(id)
        return {'message': message}, 200
    except Exception as e:
        return {'error': str(e)}, 500
