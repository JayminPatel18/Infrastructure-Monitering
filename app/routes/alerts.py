from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal, get_db
from app.models import Alerts
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)

@router.get("/")
def list_alerts(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return db.query(Alerts).order_by(Alerts.created_at.desc()).all()