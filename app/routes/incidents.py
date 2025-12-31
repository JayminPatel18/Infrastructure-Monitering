from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models import Incidents

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)
#  GET all incidents
@router.get("/")
def list_incidents(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return db.query(Incidents).order_by(Incidents.created_at.desc()).all()