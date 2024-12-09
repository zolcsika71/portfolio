from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

DANELFIN_API_KEY = os.getenv("DANELFIN_API_KEY")
BASE_URL = os.getenv("BASE_URL")

if not DANELFIN_API_KEY:
    raise ValueError("API_KEY not set in .env file")

if not BASE_URL:
    raise ValueError("BASE_URL not set in .env file")
