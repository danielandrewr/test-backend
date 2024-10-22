from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from pydantic import BaseModel
from Auth.token_handler import create_token
from Auth.hash import verify_password, get_password_hashed
from config import TOKEN_EXPIRE_IN_MINUTES

class LoginRequest(BaseModel):
    username: str
    password: str

router = APIRouter()

test_user = {
    "test_1": {
        "username": "test_1",
        "email": "test123@gmail.com",
        "hashed_pass": get_password_hashed("testpassword")
    }
}

def authenticate_user(test_user: dict, username: str, password: str):
    user = test_user.get(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_pass"]): 
        return False
    
    return user

@router.post("/request_token")
async def request_token(data: LoginRequest):
    user = authenticate_user(test_user, data.username, data.password)
    if not user:
        print("Wrong password")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized access",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    token_expires = timedelta(minutes=TOKEN_EXPIRE_IN_MINUTES)
    token = create_token(data={"sub": user["username"]}, expires_delta=token_expires)

    return {"token": token}