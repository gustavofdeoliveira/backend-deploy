from enum import Enum

# Body schema validation
class Schema(Enum):
   REGISTER = {
      "type": "object",
      "properties": {
         "name": {"type": "string"}      
      },
      "required": ["name"]
   }
   UPDATE = {
      "type": "object",
      "properties": {
         "id": {"type": "integer"},
         "name": {"type": "string"}     
      },
      "required": ["id","name"]
   }
   DELETE = {
      "type": "object",
      "properties": {
         "id": {"type": "integer"}
      },
      "required": ["id"]
   }
   GET = {
      "type": "object",
      "properties": {
         "id": {"type": "integer"}
      },
      "required": ["id"]
   }
