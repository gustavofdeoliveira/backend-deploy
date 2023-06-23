from __init__ import db
from prisma import Prisma
from datetime import datetime

# This function creates a route with the provided details and returns a route.
def create_route(name: str) -> Prisma.route:
    data = { 'name': name }
    db.route.create(data)
    route = db.route.find_first(order={'id': 'desc'})
    return route

# This function gets all the routes in the database and returns a list of routes.
def get_routes() -> list[Prisma.route]:
    routes = db.route.find_many()
    if not routes:
        raise NameError('Table routes is empty')
    else:
        return routes

# This function gets a route with the provided id and returns a route.
def get_route(id) -> Prisma.route:
    route = db.route.find_first(where={'id': id})
    if not route:
        raise NameError('Route not exists')
    else:
        return route

# This function updates a route with the provided details and returns a message.
def update_route(id: int, name: str, createdAt:datetime) -> str:
    route = db.route.find_first(where={'id': id})
    if not route:
        raise NameError(f'Route not exists with this id: {id}')
    else:
        data = {
            'id':id,
            'name': name
        }
        db.route.update(where={'id': id}, data=data)
        return f'Route {id} updated with success!'

# This function deletes the route with the provided id and returns a message.
def delete_route(id: int) -> str:
    route = db.route.find_first(where={'id': id})
    if not route:
        raise NameError(f'Route not exists with this id: {id}')
    else:
        db.route.delete(where={'id': id})
        return f'Route {id} deleted with success!'