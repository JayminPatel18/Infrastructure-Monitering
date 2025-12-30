# 9 Create alert Processor -> This processes latest metrics

from app.database import SessionLocal
from app.models import SystemMetric
from app.alert_service import generate_alert
from sqlalchemy import desc
from app.logger import logger

db = SessionLocal()

def process_latest_metrics():
    
    try:
        logger.info("Started processing latest system metrics")
        metrics = (
            db.query(SystemMetric)
            .order_by(desc(SystemMetric.timestamp))
            .limit(5)
            .all()
        )

        if not metrics:
            logger.warning("No System metrics found to process")
            return 

        for metric in metrics:
            generate_alert(metric)
        
        logger.info("Completed processing latest system metrics")
    except Exception as e:
        logger.error(f"Failed while processing metrics | Error={e}")
        raise

    finally:
        db.close()

if __name__ == "__main__":
    process_latest_metrics()