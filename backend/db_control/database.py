# backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# SQLite接続パス（tracking_app_dbフォルダ内）
#DATABASE_URL = "sqlite:///tracking_app_db/access_logs.db"

# Renderでは /tmp を使う
DB_PATH = "/tmp/access_logs.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

# エンジン作成
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # SQLiteの場合はこれ必須
)

# セッション作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# セッション取得用関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
