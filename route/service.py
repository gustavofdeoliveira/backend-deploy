from route.model import create_route, get_routes, get_route, delete_route, update_route
from pydantic import BaseModel, Field
from datetime import datetime
class Route:
    def __init__(self,id:int="", name: str="", createdAt:datetime="") -> None:
       self.id = id
       self.name = name.upper()
       self.createdAt = createdAt

    def register(self) -> str:
        try:
            create_route(name = self.name)
            return f"Route {self.name} created with success!"
        except: 
            raise NameError(f'Error to create route')
        
    def get_all(self) -> list[dict[str, str]]:
        try:
            routes = get_routes()
            response = []
            for route in routes:
                route.createdAt = route.createdAt.strftime("%d/%m/%Y %H:%M:%S")
                route = route.__dict__
                response.append(route)
            return response
        except:
            raise NameError(f'Error to get routes')
    
    def get_route(self, id: int) -> dict[str, str]:
        try:
            route = get_route(id)
            route.createdAt = route.createdAt.strftime("%d/%m/%Y %H:%M:%S")
            route = route.__dict__
            return route
        except:
            raise NameError(f'Error to get route')
        
    def update_route(self) -> str:
        try:
            update_route(id=self.id, name = self.name, createdAt=self.createdAt)
            return f"Route {self.id} updated with success!"
        except:
            raise NameError(f'Error to update route')
        
    def delete_route(self, id: int) -> str:
        try:
            delete_route(id)
            return f"Route {id} deleted with success!"
        except:
            raise NameError(f'Error to delete route')

class RouteTestCreate(BaseModel):
    name : str = "Test route"

class RouteTestUpdate(BaseModel):
    id : int = Field(example=1)
    name : str = "Test route updated"
    createdAt: datetime = datetime.now()