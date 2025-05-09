# backend/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# この database.py ファイルの絶対パス取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# プロジェクトルートから tracking_app_db/access_logs.db を指定
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, '../tracking_app_db/access_logs.db')}"

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
