from __init__ import db
from prisma import Prisma
from datetime import datetime

def create_route(name: str) -> bool:
    data = { 'name': name }
    db.route.create(data)
    return True

def get_routes() -> list[Prisma.route]:
    routes = db.route.find_many()
    if not routes:
        raise NameError('Table routes is empty')
    else:
        return routes

def get_route(id) -> Prisma.route:
    route = db.route.find_first(where={'id': id})
    if not route:
        raise NameError('Route not exists')
    else:
        return route

def update_route(id: int, name: str, createdAt:datetime) -> bool:
    route = db.route.find_first(where={'id': id})
    if not route:
        raise NameError(f'Route not exists with this id: {id}')
    else:
        data = {
            'id':id,
            'name': name
        }
        db.route.update(where={'id': id}, data=data)
        return True
    
def delete_route(id: int) -> bool:
    route = db.route.find_first(where={'id': id})
    if not route:
        raise NameError(f'Route not exists with this id: {id}')
    else:
        db.route.delete(where={'id': id})
        return True