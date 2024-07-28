import os

SECRET_KEY = os.getenv(
    "SECRET_KEY", "9b64bf7e9d2e62d992265f36cb3f3ff3363d8de6005c6d4466dfb9c044e4bc8d"
)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "AuthDB")
