from robot.service import Robot

def register(name: str, ip: str) -> tuple[dict[str, str], int]:
    try:
        robot = Robot(name=name, ip=ip)
        message = robot.register()
        return {'message': message}, 200
    except Exception as e:
        return {'error': str(e)}, 500
    
def get_robots() -> tuple[list[dict[str, str]], int]:
    try:
        robot = Robot()
        robots = robot.get_all()
        return {'robots': robots}, 200
    except Exception as e:
        return {'error': str(e)}, 500
    
def get_robot(id)-> tuple[list[dict[str, str]], int]:
    try:
        robot = Robot()
        robot = robot.get_robot(id=id)
        return {'robot': robot}, 200
    except Exception as e:
        return {'error': str(e)}, 500
    
def delete_robot(id) -> tuple[dict[str, str], int]:
    try:
        robot= Robot()
        message = robot.delete_robot(id=id)
        return {'robot': message}, 200
    except Exception as e:
        return {'error': str(e)}, 500
    
        