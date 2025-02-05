import os

# should change this value to static 
AI_PROVIDER = os.getenv("AI_PROVIDER", "openai")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DB_URL = os.getenv("DATABASE_URL")
LOG_FILE = "app.log"

WHATSAPP='WA'
TELEGRAM='TG'