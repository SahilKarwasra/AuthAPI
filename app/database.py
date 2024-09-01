from motor.motor_asyncio import AsyncIOMotorClient

from app.config import DATABASE_NAME, MONGODB_URL

client = AsyncIOMotorClient(MONGODB_URL)
db = client[DATABASE_NAME]

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
