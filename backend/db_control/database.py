# backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# SQLite接続パス（tracking_app_dbフォルダ内）
#DATABASE_URL = "sqlite:///tracking_app_db/access_logs.db"

# Renderでは /tmp を使う
#DB_PATH = "/tmp/access_logs.db"
#DATABASE_URL = f"sqlite:///{DB_PATH}"

# PostgreSQL用の接続文字列（Renderの情報に置き換えてください）
DATABASE_URL = "postgresql://<USER>:<PASSWORD>@<HOST>:<PORT>/<DB_NAME>"

engine = create_engine(DATABASE_URL)

# セッション作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# セッション取得用関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
