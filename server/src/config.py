from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class DBSettings(BaseSettings):
    POSTGRES_USER : str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD : str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER : str = os.getenv('POSTGRES_SERVER', 'localhost')
    POSTGRES_PORT : str = os.getenv('POSTGRES_PORT', 5432) 
    POSTGRES_DB : str = os.getenv('POSTGRES_DB', 'tdd')
    DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'

    
settings = DBSettings()
