# 10. Logging : In real infrastructure systems, logs are used for auditing, troubleshooting, and post-incident analysis.
# Logging ensures system observability and accountability.”

import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "system.log")

os.makedirs(LOG_DIR, exist_ok=True)

# Create formatter
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

# File handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# 🔥 Application logger
logger = logging.getLogger("infra_monitoring")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 🔴 IMPORTANT: prevent duplicate / root logging
logger.propagate = False

# 🔕 Silence SQLAlchemy logs
logging.getLogger("sqlalchemy").setLevel(logging.WARNING)
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
logging.getLogger("sqlalchemy.pool").setLevel(logging.WARNING)

print("LOGGER FILE:", LOG_FILE)