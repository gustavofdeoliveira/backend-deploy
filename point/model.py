from datetime import datetime
from __init__ import db
from prisma import Prisma

# This function creates a point with the provided details and returns a point.
def create_point(pointX: float, pointY: float, routeId: int) -> Prisma.point:
    data = {
        'pointX': pointX,
        'pointY': pointY,
        'routeId': routeId
    }
    db.point.create(data=data)
    point = db.point.find_first(order={'id': 'desc'})
    return point

# This function gets all the points in the database and returns a list of points.
def get_points(routeId: int) -> list[Prisma.point]:
    points = db.point.find_many(where={'routeId': routeId})
    if not points:
        return NameError(f'Table point is empty')
    else:
        return points

# This function deletes the points with the provided routeId and returns a message.
def delete_points(routeId: int) -> bool:
    point = db.point.find_first(where={'routeId': routeId})
    if not point:
        return f'Points not exists with this routeId: {routeId}!'
    else:
        db.point.delete_many(where={'routeId': routeId})
        return f'Points with routeId: {routeId} deleted with success!'
