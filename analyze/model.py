from __init__ import db
from datetime import datetime
from prisma import Prisma

# This function registers an analysis with the provided details and returns a message along with the HTTP status code.
def create_analyze(routeId: int, name: str, startDate: str, endDate: str, supervisor: str, operator: str,
                   robotId: int) -> Prisma.analyze:
    route = db.route.find_first(where={'id': routeId})
    if not route:
        raise NameError(f'Route not exists with this id: {routeId}')
    else:
        data = {
            "routeId": routeId,
            "name": name,
            "startDate": startDate,
            "endDate": endDate,
            "supervisor": supervisor,
            "operator": operator,
            "robotId": int(robotId)
        }
        db.analyze.create(data=data)
        analyze = db.analyze.find_first(order={'id': 'desc'})
        return analyze

# This function register a image of an analysis with the provided details and returns a message along with the HTTP status code.
def save_image(Analyzeid: int, frame: str) -> str:
    analyze = db.analyze.find_first(where={'id': Analyzeid})
    if not analyze:
        raise NameError(f'Analyze not exists with this id: {Analyzeid}')
    else:
        data = {
            "path": frame,
            "analyzeId": Analyzeid
        }
        db.image_analyse.create(data=data)
        return frame

# This function returns all the analyses in the database along with the HTTP status code.
def get_analyzes() -> list[Prisma.analyze]:
    analyzes = db.analyze.find_many()
    if not analyzes:
        raise NameError(f'Table analyzes is empty')
    else:
        return analyzes

# This function returns the analysis with the provided id along with the HTTP status code.
def get_analyze(id: int) -> Prisma.analyze:
    analyze = db.analyze.find_first(where={'id': id})
    analyze.sensor = db.sensor.find_many(where={'analyzeId': id})
    if not analyze:
        raise NameError(f'Analyze not exists with this id: {id}!')
    else:
        return analyze

# This function updates the analysis with the provided id and details and returns a message along with the HTTP status code.
def update_analyze(id: int, routeId: int, name: str, status: str, startDate: str, endDate: str, supervisor: str,
                   operator: str) -> str:
    analyze = db.analyze.find_first(where={'id': id})
    if not analyze:
        raise NameError(f'Analyze not exists with this id: {id}!')
    else:
        data = {
            'routeId': routeId,
            'name': name,
            'status': status,
            'startDate': startDate,
            'endDate': endDate,
            'supervisor': supervisor,
            'operator': operator,
        }
        print(data)
        db.analyze.update(where={'id': id}, data=data)
        return f'Analyze {id} updated with success!'

# This function deletes the analysis with the provided id and returns a message along with the HTTP status code.
def delete_analyze(id: int) -> str:
    analyze = db.analyze.find_first(where={'id': id})
    if not analyze:
        raise NameError(f'Analyze not exists with this id: {id}!')
    else:
        db.analyze.delete(where={'id': id})
        return f'Analyze {id} deleted with success!'

# This function registers a sensor reading with the provided details and returns a message along with the HTTP status code.
def create_sensor_data(id: int, sensor_data: int) -> str:
    data = {
        'analyzeId': id,
        'data': sensor_data
    }
    db.sensor.create(data=data)
    return f'New sensor reading create with success with value: {sensor_data}!'
