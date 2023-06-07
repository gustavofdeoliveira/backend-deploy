from point.model import create_point, get_points, delete_points
from pydantic import BaseModel, Field
from datetime import datetime
class Point:
    def __init__(self, pointX: float="", pointY: float="", routeId: int="", createdAt: datetime="") -> None:
        self.pointX = pointX
        self.pointY = pointY
        self.routeId = routeId
        self.createdAt = createdAt

    def register(self) -> dict[str, str]:
        try:
            point = create_point(pointX = self.pointX, pointY = self.pointY, routeId = self.routeId)
            point.createdAt = point.createdAt.strftime("%d/%m/%Y %H:%M:%S")
            point = point.__dict__
            return point
        except: 
            raise NameError(f'Error to create point')
    
    def get_all(routeId:int) -> list[dict[str, str]]:
        try:
            points = get_points(routeId)
            if not points:
                return NameError(f'Points not found')
            else:
                response = []
                for point in points:
                    point.createdAt = point.createdAt.strftime("%d/%m/%Y %H:%M:%S")
                    point = point.__dict__
                    response.append(point)
                return response
        except:
            raise NameError(f'Error to get all points')
        
    def delete_points(routeId:int) -> str:
        try:
            msg = delete_points(routeId)
            print(msg)
            if msg == False:
                return 'Points not found'
            else:
                return (f'Points deleted with routeId: {routeId}')
        except:
            raise NameError(f'Error to delete points')
        

class PointTestCreate(BaseModel):
    pointX: int = Field(example=1.52)
    pointY: int = Field(example=1.52)
    routeId: int = Field(example=1)
    