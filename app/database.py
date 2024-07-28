from motor.motor_asyncio import AsyncIOMotorClient

from app.config import DATABASE_NAME, MONGODB_URL

client = AsyncIOMotorClient(MONGODB_URL)
db = client[DATABASE_NAME]
