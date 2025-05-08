from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db_control.database import get_db
from backend.db_control import crud
from fastapi.responses import RedirectResponse
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

router = APIRouter()

@router.get("/track")
def track(uid: str, db: Session = Depends(get_db)):
    access_log = crud.update_access_log(db, uid)
    if not access_log:
        raise HTTPException(status_code=404, detail="UID not found")
    
    return RedirectResponse(url=access_log.target_url)
