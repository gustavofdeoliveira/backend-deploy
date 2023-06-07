from route.service import Route
from datetime import datetime

def register(name:str) -> tuple[dict[str, str], int]:
    try:
        route = Route(name=name)
        message = route.register()
        return {'message': message}, 200
    except Exception as e:
        return {'error': str(e)}, 500
    
def get_all() -> tuple[list[dict[str, str]], int]:
    try:
        routes = Route()
        routes = routes.get_all()
        return {'routes':routes}, 200
    except Exception as e:
        return {'error': str(e)}, 500
    
def get_route(id: int) -> tuple[dict[str, str], int]:
    try:
        route = Route()
        route = route.get_route(id)
        return {'route':route}, 200
    except Exception as e:
        return {'error': str(e)}, 500
    
def update_route(id: int, name: str, createdAt: datetime) -> tuple[dict[str, str], int]:
    try:
        route = Route(id=id, name=name, createdAt=createdAt)
        message = route.update_route()
        return {'message': message}, 200
    except Exception as e:
        return {'error': str(e)}, 500
    
def delete_route(id: int) -> tuple[dict[str, str], int]:
    try:
        route = Route()
        message = route.delete_route(id)
        return {'message': message}, 200
    except Exception as e:
        return {'error': str(e)}, 500
