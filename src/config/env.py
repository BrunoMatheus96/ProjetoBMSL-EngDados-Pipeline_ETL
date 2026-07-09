from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET = os.getenv("DATASET")
TABLE = os.getenv("TABLE")
TABLE_ID = f"{PROJECT_ID}.{DATASET}.{TABLE}"
CREDENTIALS_PATH = os.getenv("CREDENTIALS_PATH")