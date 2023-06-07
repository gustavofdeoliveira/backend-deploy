from __init__ import db
from prisma import Prisma

def create_robot(name: str, ip: str) -> bool:
    robot = db.robot.find_first(where={'ip': ip})
    if robot:
        raise NameError(f'Robot already exists with this ip: {robot}')
    data = {
            'name': name,
            'ip': ip        }
    db.robot.create(data=data)
    return True

def get_robots() -> list[Prisma.robot]:
    robots = db.robot.find_many(order={'createdAt': 'desc'})
    if not robots:
        raise NameError(f'No robots registered')
    else:
        return robots

def get_robot(id: int) -> Prisma.robot:
    robot = db.robot.find_first(where={'id': id})
    if not robot:
        raise NameError(f'Robot not exists with this id: {id}')
    else:
        return robot

def delete_robot(id: int) -> bool:
    robot = db.robot.find_first(where={'id': id})
    if not robot:
        raise NameError(f'Robot not exists with this id: {id}')
    else:
        db.robot.delete(where={'id': id})
        return True
    

    