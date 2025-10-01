import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENDPOINT = os.getenv("ENDPOINT")
    API_KEY = os.getenv("API_KEY")
    CONNECTION_STRING = os.getenv("CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")