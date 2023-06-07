from enum import Enum

# Body schema validation
class Schema(Enum):
   REGISTER = {
      "type": "object",
      "properties": {
         "routeId": {"type": "integer"},
         "name": {"type": "string"},
         "startDate": {"type": "string"},
         "endDate": {"type": "string"},
         "supervisor": {"type": "string"},
         "operator": {"type": "string"}
      },
      "required": ["routeId", "name", "startDate", "endDate", "supervisor", "operator"]
   }
   GET = {
      "type": "object",
      "properties": {
         "id": {"type": "integer"}
      },
      "required": ["id"]
   }
   DELETE = {
      "type": "object",
      "properties": {
         "id": {"type": "integer"}
      },
      "required": ["id"]
   }
   UPDATE = {
      "type": "object",
      "properties": {
         "id": {"type": "integer"},
         "routeId": {"type": "integer"},
         "name": {"type": "string"},
         "startDate": {"type": "string"},
         "endDate": {"type": "string"},
         "supervisor": {"type": "string"},
         "operator": {"type": "string"}
      },
      "required": ["id","routeId", "name", "startDate", "endDate", "supervisor", "operator"]
   }

