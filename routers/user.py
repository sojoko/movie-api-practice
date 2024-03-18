from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import HTMLResponse, JSONResponse
from schemas.user import User
from dotenv import load_dotenv
import os
load_dotenv()


user_router = APIRouter()


    
@user_router.post("/login", tags=["auth"])
def login(user: User):
    if user.username == os.getenv("username") and user.password == os.getenv("password"):
        token: str = create_token(user.model_dump())
    return JSONResponse(status_code=200, content= token)

