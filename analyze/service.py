from analyze.model import get_analyze, get_analyzes, create_analyze, update_analyze, delete_analyze, save_image, \
    create_sensor_data
from datetime import datetime, date
from pydantic import BaseModel, Field

# Class Analyze
class Analyze:
    # Constructor
    def __init__(self, id: int = "", routeId: int = "", name: str = "", status: str = "", startDate: str = "",
                 endDate: str = "", supervisor: str = "", operator: str = "", createdAt: date = "",
                 robotId: int = None) -> None:
        self.id = id
        self.routeId = routeId
        self.name = name.upper()
        self.status = status
        self.startDate = startDate
        self.endDate = endDate
        self.supervisor = supervisor.upper()
        self.operator = operator.upper()
        self.robotId = robotId
        self.createdAt = createdAt

    # This function registers an analysis with the provided details and returns an analyze.
    def register(self) -> dict[str, str]:
        try:
            analyze = create_analyze(
                routeId=self.routeId,
                name=self.name,
                startDate=self.startDate,
                endDate=self.endDate,
                supervisor=self.supervisor,
                operator=self.operator,
                robotId=self.robotId)
            analyze.createdAt = analyze.createdAt.strftime("%d/%m/%Y %H:%M:%S")
            analyze = analyze.__dict__
            return analyze
        except Exception as error:
            raise NameError(f'Error to create {self.name} analyze! Error: {error}')
        
    # This function register an image to the analysis with the provided id and returns a message.
    def register_video(self, frame: str) -> str:
        try:
            response = save_image(self.id, frame)
            return response
        except Exception as error:
            raise NameError(f'Error to save image! Error: {error}')
        
    # This function gets all the analyses in the database and returns a list of analyzes.
    def get_all(self) -> list[dict[str, str]]:
        try:
            analyzes = get_analyzes()
            if not analyzes:
                raise NameError(f'Not exists analyzes!')
            else:
                response = []
                for analyze in analyzes:
                    analyze.createdAt = analyze.createdAt.strftime("%d/%m/%Y %H:%M:%S")
                    analyze = analyze.__dict__
                    response.append(analyze)
                return response
        except Exception as error:
            raise NameError(f'Error to get analyzes! Error: {error}')
        
    # This function gets an analysis with the provided id and returns an analyze.
    def get_analyze(self) -> dict[str, str]:
        try:
            analyze = get_analyze(id=self.id)
            analyze.createdAt = analyze.createdAt.strftime("%d/%m/%Y %H:%M:%S")
            if analyze.sensor:
                for sensor in analyze.sensor:
                    sensor.createdAt = sensor.createdAt.strftime("%d/%m/%Y %H:%M:%S")
                analyze.sensor = [sensor.__dict__ for sensor in analyze.sensor]
            analyze = analyze.__dict__
            return analyze
        except Exception as error:
            raise NameError(f'Error to get analyze with this id: {self.id}! Error: {error}')
    # This function updates an analysis with the provided details and returns a message.
    def update_analyze(self) -> str:
        try:
            response = update_analyze(
                id=self.id,
                routeId=self.routeId,
                name=self.name,
                status=self.status,
                startDate=self.startDate,
                endDate=self.endDate,
                supervisor=self.supervisor,
                operator=self.operator)
            return response
        except Exception as error:
            raise NameError(f'Error to update analyze with this id: {self.id}! Error: {error}')

    # This function deletes an analysis with the provided id and returns a message.
    def delete_analyze(self, id: int) -> str:
        try:
            response = delete_analyze(id)
            return response
        except Exception as error:
            raise NameError(f'Error to delete analyze with this id: {id}! Error: {error}')

    # This function creates a sensor data with the provided details and returns a message.
    def create_sensor_data(self, sensor_data: int) -> str:
        try:
            response = create_sensor_data(
                id=self.id,
                sensor_data=sensor_data)
            return response
        except Exception as error:
            raise NameError(f'Error to update sensor data! Error: {error}')

# Class AnalyzeCreate Test
class AnalyzeTestCreate(BaseModel):
    routeId: int = Field(description="Id of route", example=1)
    name: str = "Test"
    status: str = "In Progress"
    startDate: date = date.today()
    endDate: date = date.today()
    supervisor: str = "Test supervisor"
    robotId: int = Field(description="Id of robot", example=1)
    operator: str = "Test operator"


# Class AnalyzeUpdate Test
class AnalyzeTestUpdate(BaseModel):
    id: int = Field(example=1)
    routeId: int = Field(example=1)
    name: str = "Test Update"
    status: str = "Completed"
    startDate: date = date.today()
    endDate: date = date.today()
    supervisor: str = "Test supervisor Update"
    operator: str = "Test operator Update"
