# backend/models.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AccessLog(Base):
    __tablename__ = "access_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, nullable=False)
    zebra_id = Column(String, nullable=False)
    campaign_name = Column(String, nullable=False)
    uid = Column(String, unique=True, nullable=False)
    target_url = Column(String, nullable=False)
    access_count = Column(Integer, default=0)
    last_accessed_at = Column(DateTime, nullable=True)