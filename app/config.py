# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv('MONGODB_URL', 'mongodb://localhost:27017')
SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def load_config():
    # Example function content
    return {
        "SECRET_KEY": "your_secret_key",
        "ALGORITHM": "HS256",
        "ACCESS_TOKEN_EXPIRE_MINUTES": 30
    }