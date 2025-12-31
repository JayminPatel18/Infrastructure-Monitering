# 15 Protect Existing Endpoints

from app.dependencies import get_current_user
from fastapi import Depends, FastAPI

from app.models import Incidents
from app.routes.auth_routes import get_db
from sqlalchemy.orm import Session

# app = FastAPI() 

# @app.get("/incidents")
# def get_incidents(
#     current_user: dict = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     return db.query(Incidents).all()

from fastapi import FastAPI
from app.routes import auth_routes, metrics, alerts, incidents

app = FastAPI(title="Infrastructure Monitoring System")

app.include_router(auth_routes.router)
app.include_router(metrics.router)
app.include_router(alerts.router)
app.include_router(incidents.router)