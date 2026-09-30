import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "FitBuddy AI")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

settings = Settings()