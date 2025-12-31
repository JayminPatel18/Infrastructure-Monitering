# 12 : JWT TOKEN UTILS
from datetime import datetime, timedelta
from jose import jwt
import pytz

ist = pytz.timezone("Asia/Kolkata")

SECRET_KEY = "infra-monitoring-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(ist) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
