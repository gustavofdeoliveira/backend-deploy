from datetime import datetime, timedelta, date
from pydantic import BaseModel, Field
import bcrypt
import jwt
from user.model import create_user, get_user_by_email, get_user_by_id

# Class User
class User:
    # Constructor
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
    # This function registers a user with the provided details and returns a user.
    def register(self) -> str:
        # Encrypting the password
        password = str(self.password)
        password = password.encode('UTF_8')
        password_crypt = bcrypt.hashpw(password, bcrypt.gensalt(10))
        password_crypt = password_crypt.decode("utf-8")

        # Creating the user
        create_user(name=self.name, email=self.email, password=password_crypt)

        return f"User: {self.name}, created successfully"
    
    # This function gets the user with the provided id and returns a user.
    def login(self) -> tuple[str, str]:
        try:
            user = get_user_by_email(email=self.email)
        except:
            raise NameError(f"User does not exists with the email: {self.email}")
        if bcrypt.checkpw(password=str(self.password).encode('UTF_8'),
                          hashed_password=str(user.password).encode('UTF_8')):
            payload_data = {'id': user.id, "exp": datetime.utcnow() + timedelta(hours=2)}
            token = jwt.encode(payload=payload_data, key='secret')

            return f"Thank you for login!", token

        raise NameError("Incorrect password!")
    
    # This function gets the user with the provided id and returns a user.
    def get_user(self, id: str) -> dict[str, str]:
        user = get_user_by_id(id=id)
        return user

    # def login(self) -> str:
    #    try:
    #       models.already_exists_by_email(email=self.email)
    #    except:
    #       raise NameError(f"User does not exists with the email: {self.email}")

    #    user = models.get_user_by_email(email=self.email)
    #    if bcrypt.checkpw(str(self.password).encode('UTF_8'), str(user.password).encode('UTF_8')):
    #       payload_data = {'id': user.id, "exp": datetime.utcnow() + timedelta(hours=2)}
    #       token = jwt.encode(payload=payload_data, key='secret')

# Class UserTest
class UserTestCreate(BaseModel):
    name : str = "Test operator Update"
    email: str = "teste@teste.com"
    password: str = "teste123"

# Class UserTest
class UserTestLogin(BaseModel):
    email: str = "teste@teste.com"
    password: str = "teste123"