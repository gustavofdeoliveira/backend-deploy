from robot.model import create_robot, get_robots, get_robot, delete_robot
from pydantic import BaseModel, Field

class Robot:
    def __init__(self, name: str="", ip:str="") -> None:
       self.name = name.upper()
       self.ip = ip.upper()

    def register(self) -> str:
        try:
            create_robot(ip = self.ip, name = self.name)
            return f"Robot {self.name} created with success!"
        except: 
            raise NameError(f'Error to create point')
    
    def get_all(self) -> list[dict[str, str]]:
        try:
            robots = get_robots()
            response = []
            for robot in robots:
                robot.createdAt = robot.createdAt.strftime("%d-%m-%Y %H:%M:%S")
                robot = robot.__dict__
                response.append(robot)
            return response
        except:
            raise NameError(f'Error to get all robots')
        
    def get_robot(self, id:int) -> dict[str, str]:
        try:
            robot = get_robot(id)
            robot.createdAt = robot.createdAt.strftime("%d-%m-%Y %H:%M:%S")
            return robot.__dict__
        except:
            raise NameError(f'Error to get robot')
        
    def delete_robot(self, id:int) -> str:
        try:
            delete_robot(id)
            return f"Robot deleted with success!"
        except:
            raise NameError(f'Error to delete robot')
        
class RobotTestCreate(BaseModel):
    name: str = "Robot Test"
    ip : str = "112.224.131.11"