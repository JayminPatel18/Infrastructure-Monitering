# 3. create database tables

from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String(50), unique = True, nullable = False)
    password = Column(String(255), nullable = False)
    role = Column(String(20))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class SystemMetric(Base):
    __tablename__ = "system_metrics"

    id = Column(Integer, primary_key = True, index = True)
    metric_type = Column(String(30))
    metric_value = Column(Float)
    status = Column(String(20))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class Alerts(Base):
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True, index = True)
    metric_id = Column(Integer, ForeignKey("system_metrics.id"))
    severity = Column(String(20))
    message = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default= func.now())

class Incidents(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index = True)
    alert_id = Column(Integer, ForeignKey("alerts.id"))
    status = Column(String(20))
    assigned_to = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    resolved_at = Column(DateTime(timezone=True), nullable=True)

    
