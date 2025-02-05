import psycopg2
import logging
from config import DB_URL

logging.basicConfig(filename="app.log", level=logging.ERROR)

try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
except Exception as e:
    logging.error(f"Database connection error: {e}")
    raise
