from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from starlette.types import ASGIApp
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import JSONResponse


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(content=str(e.detail), status_code=e.status_code)
        