import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    DB_USER = "banki"
    DB_PASSWORD = "password"
    DB_HOST = "192.168.9.72"
    DB_PORT = "1521"
    DB_SERVICE =  "xepdb1"