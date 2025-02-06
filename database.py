import psycopg2
import logging
from config_integration import DB_URL, DB_USER, DB_PASS
from config import LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=logging.ERROR)

try:
    conn = psycopg2.connect(
        dbname=DB_URL,
        user=DB_USER,
        password=DB_PASS
    )
    cursor = conn.cursor()
except Exception as e:
    logging.error(f"Database connection error: {e}")
    raise