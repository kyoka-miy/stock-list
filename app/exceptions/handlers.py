from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.exceptions.app_exception import AppException


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [
        {
            "field": e["loc"][-1],
            "message": e["msg"]
        }
        for e in exc.errors()
    ]
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation error",
            "details": errors
        }
    )


async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=400,
        content={"message": exc.message}
    )
