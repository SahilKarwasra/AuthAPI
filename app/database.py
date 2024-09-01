from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from app.config import DATABASE_NAME, MONGODB_URL

client = AsyncIOMotorClient(MONGODB_URL, server_api=ServerApi("1"))
db = client[DATABASE_NAME]

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
