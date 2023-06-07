from functools import wraps

import jwt
from sanic.request import Request
from sanic.response import HTTPResponse, json


def auth(f):
    @wraps(f)
    def auth_function(request: Request) -> HTTPResponse:
        try:
            # Token must be passed as 'Bearer <token>' in the header
            # token = request.cookies.get('token')
            token = request.headers.Bearer
            # Decoding the token with the secret key
            decoded = jwt.decode(token, key='secret', algorithms=['HS256', ])
            # Adding the user id to the request context
            request.ctx.id = decoded['id']

            return f(request)
        # If the token is invalid, return an error message as JSON
        except Exception as err:
            return json({'type': 'error', 'message': str(err)}, status=401)

    return auth_function
