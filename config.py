"""Load config variable from environment file"""
import os
from dotenv import load_dotenv

load_dotenv()

APP_PORT = os.environ.get("APP_PORT", 7001)
DB_URL = os.environ.get("DATABASE_URL")
DB_NAME = os.environ.get("DATABASE_NAME")
