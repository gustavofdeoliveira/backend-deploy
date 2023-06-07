from analyze.model import get_analyze, get_analyzes, create_analyze, update_analyze, delete_analyze
from datetime import datetime, date
from pydantic import BaseModel, Field

class Analyze:
    def __init__(self,id:int="", routeId: int="", name: str="", startDate: str="", endDate: str="", supervisor: str="",operator: str="", createdAt: date="") -> None:
        self.id = id
        self.routeId = routeId
        self.name = name.upper()
        self.startDate = startDate
        self.endDate = endDate
        self.supervisor = supervisor.upper()
        self.operator = operator.upper()
        self.createdAt = createdAt

    def register(self) -> dict[str, str]:
        try:
            analyze = create_analyze(routeId = self.routeId, name = self.name, startDate = self.startDate, endDate = self.endDate, supervisor = self.supervisor, operator = self.operator)
            analyze.createdAt = analyze.createdAt.strftime("%d/%m/%Y %H:%M:%S")
            analyze = analyze.__dict__
            return analyze
        except: 
            raise NameError(f'Error to create {self.name} analyze!')
    
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
        except:
            raise NameError(f'Error to get analyzes!')
    
    def get_analyze(self) -> dict[str, str]:
        try:
            analyze = get_analyze(id=self.id)
            print(self.id, analyze)
            analyze.createdAt = analyze.createdAt.strftime("%d/%m/%Y %H:%M:%S")
            analyze = analyze.__dict__
            return analyze
        except:
            raise NameError(f'Error to get analyze with this id: {id}')
    
    def update_analyze(self) -> str:
        try:
            update_analyze(id = self.id, routeId = self.routeId, name = self.name, startDate = self.startDate, endDate = self.endDate, supervisor = self.supervisor, operator = self.operator, createdAt = self.createdAt)
            return f"Analyze {self.id} updated with success!"
        except:
            raise NameError(f'Error to update analyze with this id: {self.id}')
        
    def delete_analyze(self, id: int) -> str:
        try:
            delete_analyze(id)
            return f"Analyze {id} deleted with success!"
        except:
            raise NameError(f'Error to delete analyze with this id: {id}')
        
class AnalyzeTestCreate(BaseModel):
    routeId: int = Field(description="Id of route", example=1)
    name: str = "Test"
    startDate: date = date.today()
    endDate: date = date.today()
    supervisor: str = "Test supervisor"
    operator : str = "Test operator"

class AnalyzeTestUpdate(BaseModel):
    id: int = Field(example=6)
    routeId: int = Field(example=1)
    name: str = "Test Update"
    startDate: date = date.today()
    endDate: date = date.today()
    supervisor: str = "Test supervisor Update"
    operator : str = "Test operator Update"
    createdAt: datetime = datetime.today()
