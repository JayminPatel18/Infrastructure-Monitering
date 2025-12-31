# 7. Create Test Script for Metrics
from app.services.metrics_service import ingest_metric

# CPU Metrics
ingest_metric("CPU", 45)
ingest_metric("CPU", 78)
ingest_metric("CPU", 92)

# Memory Metrics
ingest_metric("Memory", 60)
ingest_metric("Memory", 88)
ingest_metric("Memory", 95)

# Disk Metrics
ingest_metric("DISK", 70)
ingest_metric("DISK", 85)
ingest_metric("DISK", 93)

# implemented a metrics ingestion service that evaluates system metrics using threshold-based rules and stores classified health states in PostgreSQL using SQLAlchemy.