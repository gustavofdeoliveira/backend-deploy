from point.service import Point

def register(pointX: float, pointY: float, routeId:int) -> tuple[dict[str, str], int]:
    try:
        point = Point(pointX=pointX, pointY=pointY, routeId=routeId)
        message = point.register()
        return {'message': message}, 200
    except Exception as e:
        return {'error': str(e)}, 500
    
def get_points(routeId: int) -> tuple[list[dict[str, str]], int]:
    try:
        points = Point.get_all(routeId=routeId)
        return {'points': points}, 200
    except Exception as e:
        return {'error': str(e)}, 500
    
def delete_points(routeId: int):
    try:
        point = Point.delete_points(routeId=routeId)
        return {'point': point}, 200
    except Exception as e:
        return {'error': str(e)}, 500