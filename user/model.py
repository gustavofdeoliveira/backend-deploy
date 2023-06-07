from __init__ import db
from prisma import Prisma


def create_user(name: str, email: str, password: str) -> bool:
    data = {
        'name': name,
        'email': email,
        'password': password
    }
    # Checking if the user already exists
    try:
        get_user_by_email(email=email)
    except:
        db.user.create(data=data)
        return True
    raise NameError(f"User already exists with the email: {email}")


def get_user_by_email(email: str) -> Prisma.user:
    try:
        user = db.user.find_unique(where={'email': email})
        if user:
            return user
        raise Exception(f"User does not exists with the email: {email}")
    except:
        raise NameError(f"User does not exists with the email: {email}")


def get_user_by_id(id: str) -> dict[str, str]:
    try:
        user = db.user.find_unique(where={'id': id})
        user.createdAt = user.createdAt.strftime("%d-%m-%Y %H:%M:%S")
        user.updatedAt = user.updatedAt.strftime("%d-%m-%Y %H:%M:%S")
        return user.__dict__
    except:
        raise NameError(f"User does not exists with the id: {id}")

# class User_models:
#    from app import db as prisma_config
#    db = prisma_config
#    user = db.user

#    def __init__(self, name: str, email: str, password: str):
#       self.name = name
#       self.email = email
#       self.password = password

#    def create_user(self):
#       data = {
#          'name': self.name,
#          'email': self.email,
#          'password': self.password
#       }
#       return User_models.user.create(data=data)

#    def get_all_users(self):
#       return self.user.find_many()

#    def get_user_by_id(self, user_id):
#       return self.user.find_unique(id=user_id)

#    def get_user_by_email(self, email):
#       return self.user.find_unique(email=email)

#    def update_user(self, user_id, user):
#       return self.user.update(id=user_id, data=user)

#    def delete_user(self, user_id):
#       return self.user.delete(id=user_id)
