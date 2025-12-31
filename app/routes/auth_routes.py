# 13 LOGIN API
from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session

from app.database import SessionLocal, get_db
from app.models import User
from app.core.auth import verify_password
from app.core.jwt_utils import create_access_token

router = APIRouter()

@router.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
    ):
    
    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code = 401, detail = "Invalid credentials")

    token = create_access_token({"sub": user.username, "role": user.role})

    return {
        "access_token": token,
        "token_type": "bearer"
    }