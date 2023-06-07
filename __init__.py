# This file have the purpose to set any configuration that is needed before running the app.
# If any configuration is not needed, it should be empty.
from prisma import Prisma

db = Prisma(auto_register=True)
db.connect()