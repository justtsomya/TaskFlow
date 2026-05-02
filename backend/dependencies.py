from fastapi import HTTPException
from jose import jwt
from config import SECRET_KEY, ALGORITHM

def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid Token")

def admin_only(user: dict):
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
    return user