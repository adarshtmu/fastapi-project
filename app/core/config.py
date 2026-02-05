import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = 'Car Price API'
    API_KEY = os.getenv('API_KEY','demo-key')
    JWT_ALGORITHM = 'HS256'
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key-change-in-production')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
    MODEL_PATH = 'app/model/model.joblib'


settings= Settings()
    
