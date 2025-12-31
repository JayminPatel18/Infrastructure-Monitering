# 8. Alert Generation  
# Alert Rules
# Create alert if status is WARNING or CRITICAL
# One active alert per metric type
# Do NOT create duplicate alerts
# Severity = status


from app.database import SessionLocal
from app.models import Alerts, SystemMetric
from sqlalchemy import desc

from app.services.incident_service import create_incident_from_alert
from app.logger import logger

db = SessionLocal()

# Check if alert already exists for metric type
def alert_exists(metric_type):
    return db.query(Alerts).join(SystemMetric).filter(
        SystemMetric.metric_type == metric_type
    ).first()


# Create Alert Logic
def generate_alert(metric: SystemMetric):

    if metric.status == "NORMAL":
        return None
    
    # Prevent duplicate alerts
    if alert_exists(metric.metric_type):
        #print(f"[ALERT EXISTS] {metric.metric_type}")
        logger.warning(f"Alert already exists | Metric={metric.metric_type}")
        return None
    
    alert = Alerts(
        metric_id = metric.id,
        severity = metric.status,
        message = f"{metric.metric_type} usage is {metric.status}"
    )

    try:
        db.add(alert)
        db.commit()
        db.refresh(alert)

        # Log alert creation
        logger.info(
            f"ALert created | Metric={metric.metric_type} | Severity={metric.status}"
        )

        # print(
        #     f"[ALERT CREATED]"
        #     f"Metric = {metric.metric_type}, Severity = {metric.status}"
        # )

        # INCIDENT ESCALATION
        if alert.severity == "CRITICAL":
            create_incident_from_alert(alert)

        return alert
    
    except Exception as e:
        logger.error(
            f"Alert creation failed | Metric={metric.metric_type} | Error={e}"
        )
        db.rollback()
        raise