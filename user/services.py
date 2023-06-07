from datetime import datetime, timedelta, date
from pydantic import BaseModel, Field
import bcrypt
import jwt
from user.model import create_user, get_user_by_email, get_user_by_id


class User:

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    def register(self) -> str:
        # Encrypting the password
        password = str(self.password)
        password = password.encode('UTF_8')
        password_crypt = bcrypt.hashpw(password, bcrypt.gensalt(10))
        password_crypt = password_crypt.decode("utf-8")

        # Creating the user
        create_user(name=self.name, email=self.email, password=password_crypt)

        return f"User: {self.name}, created successfully"

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


class UserTestCreate(BaseModel):
    name : str = "Test operator Update"
    email: str = "teste@teste.com"
    password: str = "teste123"

class UserTestLogin(BaseModel):
    email: str = "teste@teste.com"
    password: str = "teste123"