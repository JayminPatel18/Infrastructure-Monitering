# 9. add incident management : alerts indicate a problem, incidents reprent action taken on that problem

from datetime import datetime
from app.database import SessionLocal
from app.models import Incidents

from app.logger import logger

import pytz


ist = pytz.timezone("Asia/Kolkata")

db = SessionLocal()

def create_incident_from_alert(alert):
    # Create incident only for CRITICAL alerts

    incidents = Incidents(
        alert_id = alert.id,
        status = "OPEN",
        assigned_to = None,
        created_at = datetime.now(ist),
        resolved_at=None
    )

    try:
        db.add(incidents)
        db.commit()
        db.refresh(incidents)   # ✅ pass the instance

        # Critical log for incident creation
        logger.critical(
            f"Incident created | AlertID={alert.id} | Status=OPEN"
        )

        print(f"[INCIDENTS CREATED] Alert ID = {alert.id}")

        return incidents
    
    except Exception as e:
        logger.error(
            f"Incident creation failed | AlertID={alert.id} | Error={e}"
        )
        db.rollback()
        raise

    finally:
        db.close()