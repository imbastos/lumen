import os

from dotenv import load_dotenv

load_dotenv()
SQLITE_FILE = os.getenv("SQLITE_FILE")
