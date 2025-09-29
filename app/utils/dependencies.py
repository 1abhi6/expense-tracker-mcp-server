from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.database import SessionLocal
from .auth import decode_access_token

# The tokenUrl must match the full path of your login route
print("HELLO FROM dependencies.py")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
print("OAuth2PasswordBearer FROM CODE: ", oauth2_scheme)

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return int(payload["sub"])  # this is the user_id

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
