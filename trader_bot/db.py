import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
        return conn
    except Exception as e:
        print(f"❌ 連線資料庫失敗: {e}")
        return None
