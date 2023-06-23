from point.model import create_point, get_points, delete_points
from pydantic import BaseModel, Field
from datetime import datetime
# Class Point


class Point:
    # Constructor
    def __init__(self, pointX: float = "", pointY: float = "", routeId: int = "", createdAt: datetime = "") -> None:
        self.pointX = pointX
        self.pointY = pointY
        self.routeId = routeId
        self.createdAt = createdAt
    
    # This function creates a point with the provided details and returns a point.
    def register(self) -> dict[str, str]:
        try:
            point = create_point(
                pointX=self.pointX,
                pointY=self.pointY, 
                routeId=self.routeId)
            point.createdAt = point.createdAt.strftime("%d/%m/%Y %H:%M:%S")
            point = point.__dict__
            return point
        except Exception as error:
            raise NameError(f'Error to create point! Error: {error}')

    # This function gets all the points in the database and returns a list of points.
    def get_all(routeId: int) -> list[dict[str, str]]:
        try:
            points = get_points(routeId)
            if not points:
                return NameError(f'Points not found')
            else:
                response = []
                for point in points:
                    point.createdAt = point.createdAt.strftime(
                        "%d/%m/%Y %H:%M:%S")
                    point = point.__dict__
                    response.append(point)
                return response
        except Exception as error:
            raise NameError(f'Error to get all points! Error: {error}')

    # This function deletes the points with the provided routeId and returns a message.
    def delete_points(routeId: int) -> str:
        try:
            response = delete_points(routeId)
            return response
        except Exception as error:
            raise NameError(f'Error to delete points! Error: {error}')


# Class PointTestCreate 
class PointTestCreate(BaseModel):
    pointX: int = Field(example=1.52)
    pointY: int = Field(example=1.52)
    routeId: int = Field(example=1)
