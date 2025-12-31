from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.dependencies import get_current_user
from app.database import get_db
from app.services.metrics_service import ingest_metric

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"]
)

# Request Body Schema
class MetricCreate(BaseModel):
    metric_type: str
    value: float


@router.post("/")
def add_metric(
    metric: MetricCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return ingest_metric(metric.metric_type, metric.value, db)
