import oracledb
from config import Config

def get_connection():
    dsn = f"{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_SERVICE}"
    return oracledb.connect(
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        dsn=dsn
    )