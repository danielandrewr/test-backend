from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from config import SECRET_KEY, TOKEN_EXPIRE_IN_MINUTES
from datetime import datetime, timedelta, timezone

oauth2 = OAuth2PasswordBearer(tokenUrl="request_token")

def create_token(data: dict, expires_delta: timedelta = None):
    encoded_data = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRE_IN_MINUTES)

    encoded_data.update({"exp": int(expire.timestamp())})
    encoded_jwt = jwt.encode(encoded_data, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def verify_token(token: str = Depends(oauth2)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Failed to validate",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username: str = data.get("sub")
        print(f"Decoded Payload: {data}")
        if username is None: raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    return username
