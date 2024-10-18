# config.py
import os
from pymongo import MongoClient
from pydantic import BaseModel, Field
from .env_vars import MONGODB_URL,DB_NAME


client = MongoClient(MONGODB_URL)

db = [DB_NAME]

employee_collection = db["Employee"]
