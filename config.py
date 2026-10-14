import os

from dotenv import load_dotenv

load_dotenv()
SQLITE_FILE = os.getenv("SQLITE_FILE")
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")