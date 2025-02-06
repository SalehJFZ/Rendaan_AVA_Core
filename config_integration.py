import os
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

############## AI ##############
AI_PROVIDER = "METIS-OPENAI"
METIS_OPENAI_KEY = os.getenv("METIS_OPENAI_API_KEY")
# DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

############## DB ##############
DB_HOST = "8f904210-0c32-4361-86a9-325228fea1fa.hsvc.ir"
DB_PORT = "32215"
DB_NAME = "ava"  # نام پایگاه داده خود را وارد کنید
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

############## CL ##############
WA_API_URL = "https://messenger-api.com/send"
TG_API_URL = "https://messenger-api2.com/send"