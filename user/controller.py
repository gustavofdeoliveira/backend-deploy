from user.services import User


# This function registers a user with the provided details and returns a message.
def register(email: str, password: str, name: str) -> tuple[dict[str, str], int]:
    try:
        user = User(name=name, email=email, password=password)
        message = user.register()
        return {'message': message}, 200
    except Exception as e:
        return {'error': str(e)}, 500

# This function logs in a user with the provided details and returns a message.
def login(email: str, password: str) -> tuple[dict[str, str], int]:
    try:
        user = User(name=None, email=email, password=password)
        message, token = user.login()
        return {'message': message, 'token': token}, 200
    except NameError as err:
        return {'error': str(err)}, 404
    except Exception as e:
        return {'error': str(e)}, 500

# This function gets all the users in the database and returns a list of users.
def get_user(id: str) -> tuple[dict[str, str], int]:
    try:
        user = User(name=None, email=None, password=None)
        user_data = user.get_user(id=id)
        return user_data, 200
    except Exception as err:
        return {'error': str(err)}, 500
