# 6.  Calculate metric status
# Insert metrics into DB
# Acts as business logic layer

from datetime import datetime
from app.database import SessionLocal
from app.models import SystemMetric
from sqlalchemy.orm import Session

import pytz

ist = pytz.timezone("Asia/Kolkata")

from app.logger import logger


db = SessionLocal()

# Status Calculation Logic
def calculate_status(metric_type, value):
    metric_type = metric_type.upper()

    if metric_type == "CPU":
        if value < 70:
            return "NORMAL"
        elif value < 85:
            return "WARNING"
        else: 
            return "CRITICAL"
    elif metric_type == "MEMORY":
        if value < 75:
            return "NORMAL"
        elif value < 90:
            return "WARNING"
        else:
            return "CRITICAL"
    elif metric_type == "DISK":
        if value < 80:
            return "NORMAL"
        elif value < 90:
            return "WARNING"
        else: 
            return "CRITICAL"
    
    return "UNKNOWN"

# Metric Ingestion Logic
def ingest_metric(metric_type, value, db: Session):
    status = calculate_status(metric_type, value)

    metric = SystemMetric(
        metric_type = metric_type,
        metric_value = value,
        status = status, 
        timestamp = datetime.now(ist)
    )

    try:
 
        db.add(metric)
        db.commit()
        db.refresh(metric)   # ✅ pass the instance
    

        logger.info(
            f"Metric Ingested | Type={metric_type} | Value={value} | Status={status}"
        )


        print(
            f"[METRIC INGESTED] "
            f"Type = {metric_type}, Value = {value}, Status = {status}"
        )

        return metric
    
    except Exception as e:
        logger.error(f"Metric ingestion failed | Type={metric_type} | Error={e}")
        db.rollback()
        raise

    finally:
        db.close()