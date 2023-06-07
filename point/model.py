from datetime import datetime
from __init__ import db
from prisma import Prisma

def create_point(pointX: float, pointY: float, routeId: int) -> Prisma.point:   
    data = {
                'pointX': pointX,
                'pointY': pointY,
                'routeId': routeId
    }
    db.point.create(data=data)
    point = db.point.find_first(order={'id': 'desc'})
    return point
    
def get_points(routeId: int) -> list[Prisma.point]:
    points = db.point.find_many(where={'routeId': routeId})
    if not points:
        return NameError(f'Table point is empty')
    else:
        return points
    
def delete_points(routeId: int) -> bool:
    point = db.point.find_first(where={'routeId': routeId})
    if point == None or not point:
        return False
    else:
        db.point.delete_many(where={'routeId': routeId})
        return True
    