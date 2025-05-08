# backend/crud.py
from sqlalchemy.orm import Session
from backend.db_control.models import AccessLog
from datetime import datetime

# UIDを新規登録する
def create_uid(db: Session, client_id: int, zebra_id: str, campaign_name: str, uid: str, target_url: str):
    access_log = AccessLog(
        client_id=client_id,
        zebra_id=zebra_id,
        campaign_name=campaign_name,
        uid=uid,
        target_url=target_url,
        access_count=0,
        last_accessed_at=None
    )
    db.add(access_log)
    db.commit()
    db.refresh(access_log)  # 登録後のオブジェクト更新
    return access_log

# UIDを元にアクセスカウントを1増やす
def update_access_log(db: Session, uid: str):
    access_log = db.query(AccessLog).filter(AccessLog.uid == uid).first()
    if access_log:
        access_log.access_count += 1
        access_log.last_accessed_at = datetime.now()
        db.commit()
        db.refresh(access_log)
    return access_log

# 全アクセスログを取得（zebra_idまたはcampaign_nameで絞り込み可能）
def get_all_logs(db: Session, zebra_id: str = None, campaign_name: str = None):
    query = db.query(AccessLog)
    
    if zebra_id:
        query = query.filter(AccessLog.zebra_id == zebra_id)
    if campaign_name:
        query = query.filter(AccessLog.campaign_name == campaign_name)

    return query.all()
