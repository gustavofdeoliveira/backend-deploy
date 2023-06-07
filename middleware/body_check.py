from enum import Enum
from functools import wraps

from jsonschema import validate, ValidationError
from sanic.request import Request
from sanic.response import json


def validate_body(schema: Enum):
    def wraper(f):
        @wraps(f)
        def validate_body_function(request: Request):
            try:
                data = request.json
                validate(data, schema)
                return f(request)
            except ValidationError as e:
                return json({"error": str(e.message)}, 400)

        return validate_body_function

    return wraper
