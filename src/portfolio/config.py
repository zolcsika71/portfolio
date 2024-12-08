from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

if not API_KEY or not BASE_URL:
    raise ValueError("API_KEY or BASE_URL not set in .env file")
