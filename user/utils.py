from enum import Enum

# Body schema validation
class Schema(Enum):
   LOGIN = {
      "type": "object",
      "properties": {
         "email": {"type": "string"},
         "password": {"type": "string"}
      },
      "required": ["email", "password"]
   }
   REGISTER = {
      "type": "object",
      "properties": {
         "email": {"type": "string"},
         "password": {"type": "string"},
         "name": {"type": "string"}
      },
      "required": ["email", "password", "name"]
   }