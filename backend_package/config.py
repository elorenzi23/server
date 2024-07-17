import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DEV_DATABASE_URL = os.getenv('DEV_DATABASE_URL')
    PROD_DATABASE_URL = os.getenv('PROD_DATABASE_URL')


settings = Settings()
