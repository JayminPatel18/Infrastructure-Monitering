# 4. create table automatically

from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

print("Tables created successfully")

# SQLAlchemy’s create_all() is idempotent. 
# It checks for existing tables and only creates missing ones, so running it multiple times does not duplicate tables or affect existing data.
# SQLAlchemy’s create_all() safely creates only new tables. 
# Existing tables and data are preserved. For schema changes, migration tools like Alembic are used

# SQLAlchemy requires proper URL encoding for credentials. I resolved URL parsing issues by safely encoding the password and structuring the connection string correctly.

# For development and testing, I inserted controlled dummy metrics using SQL in pgAdmin. 
# These values simulate normal and abnormal system behavior and help validate alerting and incident workflows.