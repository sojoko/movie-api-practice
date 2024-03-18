
from fastapi.security import HTTPBearer
from fastapi import HTTPException, Request
from utils.jwt_manager import create_token, validate_token

class JWTBearer(HTTPBearer):
   async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        print(data)
        if data['username'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="You don't have permission to access")