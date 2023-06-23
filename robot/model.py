from __init__ import db
from prisma import Prisma
from analyze.service import Analyze

# This function creates a robot with the provided details and returns a robot.
def create_robot(name: str, ip: str) -> bool:
    robot = db.robot.find_first(where={'ip': ip})
    if robot:
        raise NameError(f'Robot already exists with this ip: {ip}!')
    data = {
        'name': name,
        'ip': ip
    }
    db.robot.create(data=data)
    return f'Robot {name} created with success!'

# This function gets all the robots in the database and returns a list of robots.
def get_robots() -> list[Prisma.robot]:
    robots = db.robot.find_many(order={'createdAt': 'desc'})
    if not robots:
        raise NameError(f'No robots registered!')
    else:
        return robots

# This function gets a robot with the provided id and returns a robot.
def get_robot(id: int) -> Prisma.robot:
    robot = db.robot.find_first(where={'id': id})
    robot.Analyze = db.analyze.find_many(where={'robotId': id})
    if not robot:
        raise NameError(f'Robot not exists with this id: {id}!')
    else:
        return robot

# This function deletes the robot with the provided id and returns a message.
def delete_robot(id: int) -> str:
    robot = db.robot.find_first(where={'id': id})
    if not robot:
        raise NameError(f'Robot not exists with this id: {id}!')
    else:
        db.robot.delete(where={'id': id})
        return f'Robot {id} deleted with success!'
