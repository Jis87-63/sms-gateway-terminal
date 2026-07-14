import os, jwt
from fastapi import APIRouter, HTTPException
from models.schemas import LoginRequest
router = APIRouter(tags=["auth"])
@router.post("/login")
def login(payload: LoginRequest):
    if payload.username == os.getenv("ADMIN_USER", "admin") and payload.password == os.getenv("ADMIN_PASSWORD", "admin123"):
        token = jwt.encode({"sub": payload.username}, os.getenv("JWT_SECRET", "change-me"), algorithm="HS256")
        return {"token": token, "user": payload.username}
    raise HTTPException(status_code=401, detail="Invalid credentials")
