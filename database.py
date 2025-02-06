import psycopg2
import logging
from config_integration import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS
from config import LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=logging.ERROR)

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cursor = conn.cursor()
except Exception as e:
    logging.error(f"Database connection error: {e}")
    raise