from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

DANELFIN_API_KEY = os.getenv("DANELFIN_API_KEY")
BASE_URL = os.getenv("BASE_URL")
TICKER = os.getenv("TICKER")
DATE = os.getenv("DATE")
SCORE = os.getenv("SCORE")
TYPE = os.getenv("TYPE")


if not DANELFIN_API_KEY:
    raise ValueError("API_KEY not set in .env file")

if not BASE_URL:
    raise ValueError("BASE_URL not set in .env file")

if not TICKER:
    raise ValueError("TICKER not set in .env file")

if not DATE:
    raise ValueError("DATE not set in .env file")

if not SCORE:
    raise ValueError("SCORE not set in .env file")

if not TYPE:
    raise ValueError("TYPE not set in .env file")
