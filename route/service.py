from route.model import create_route, get_routes, get_route, delete_route, update_route
from pydantic import BaseModel, Field
from datetime import datetime

# Class Route
class Route:
    # Constructor
    def __init__(self,id:int="", name: str="", createdAt:datetime=""):
       self.id = id
       self.name = name.upper()
       self.createdAt = createdAt

    # This function registers a route with the provided details and returns a route.
    def register(self) -> str:
        try:
            route = create_route(name = self.name)
            route.createdAt = route.createdAt.strftime("%d/%m/%Y %H:%M:%S")
            route = route.__dict__
            return route
        except Exception as error: 
            raise NameError(f'Error to create route! Error: {error}')
        
    # This function gets all the routes in the database and returns a list of routes.
    def get_all(self) -> list[dict[str, str]]:
        try:
            routes = get_routes()
            response = []
            for route in routes:
                route.createdAt = route.createdAt.strftime("%d/%m/%Y %H:%M:%S")
                route = route.__dict__
                response.append(route)
            return response
        except Exception as error:
            raise NameError(f'Error to get routes! Error: {error}')
    
    # This function gets the route with the provided id and returns a route.
    def get_route(self, id: int) -> dict[str, str]:
        try:
            route = get_route(id)
            route.createdAt = route.createdAt.strftime("%d/%m/%Y %H:%M:%S")
            route = route.__dict__
            return route
        except Exception as error:
            raise NameError(f'Error to get route! Error: {error}')
    
    # This function updates the route with the provided id and returns a message.
    def update_route(self) -> str:
        try:
            response = update_route(id=self.id, name = self.name, createdAt=self.createdAt)
            return response
        except Exception as error:
            raise NameError(f'Error to update route Error: {error}')
    
    # This function deletes the route with the provided id and returns a message.
    def delete_route(self, id: int) -> str:
        try:
            response = delete_route(id)
            return response
        except Exception as error:
            raise NameError(f'Error to delete route Error: {error}')

# Class RouteCreate Teste
class RouteTestCreate(BaseModel):
    name : str = "Test route"

# Class RouteUpdate Teste
class RouteTestUpdate(BaseModel):
    id : int = Field(example=1)
    name : str = "Test route updated"
    createdAt: datetime = datetime.now()