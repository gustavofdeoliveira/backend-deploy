from robot.model import create_robot, get_robots, get_robot, delete_robot
from pydantic import BaseModel, Field

# Class Robot
class Robot:
    # Constructor
    def __init__(self, name: str = "", ip: str = "") -> None:
        self.name = name.upper()
        self.ip = ip.upper()

    # This function registers a robot with the provided details and returns a message.
    def register(self) -> str:
        try:
            create_robot(ip=self.ip, name=self.name)
            return f"Robot {self.name} created with success!"
        except Exception as error:
            raise NameError(f'Error to create point! Error: {error}')

    # This function gets all the robots in the database and returns a list of robots.
    def get_all(self) -> list[dict[str, str]]:
        try:
            robots = get_robots()
            response = []
            for robot in robots:
                robot.createdAt = robot.createdAt.strftime("%d-%m-%Y %H:%M:%S")
                robot.updatedAt = robot.updatedAt.strftime("%d-%m-%Y %H:%M:%S")
                robot = robot.__dict__
                response.append(robot)
            return response
        except Exception as error:
            raise NameError(f'Error to get all robots! Error: {error}')

    # This function gets the robot with the provided id and returns a robot.
    def get_robot(self, id: int) -> dict[str, str]:
        try:
            robot = get_robot(id)
            robot.createdAt = robot.createdAt.strftime("%d-%m-%Y %H:%M:%S")
            robot.updatedAt = robot.updatedAt.strftime("%d-%m-%Y %H:%M:%S")
            for analyze in robot.Analyze:
                analyze.createdAt = analyze.createdAt.strftime("%d-%m-%Y %H:%M:%S")
            robot.Analyze = [analyze.__dict__ for analyze in robot.Analyze]
            return robot.__dict__
        except Exception as error:
            raise NameError(f'Error to get robot! Error: {error}')

    # This function deletes the robot with the provided id and returns a message.
    def delete_robot(self, id: int) -> str:
        try:
            response = delete_robot(id)
            return response
        except Exception as error:
            raise NameError(f'Error to delete robot! Error: {error}')

# Class RobotCreate
class RobotTestCreate(BaseModel):
    name: str = "Robot Test"
    ip: str = "112.224.131.11"
