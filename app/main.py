from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.exceptions.handlers import app_exception_handler, validation_exception_handler
from app.presentation.account_controller import router as account_router
from app.presentation.stock_controller import router as stock_router
from app.presentation.stock_list_controller import router as stock_list_router
from app.exceptions.app_exception import AppException


app = FastAPI()

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler  # type: ignore
)

app.add_exception_handler(
    AppException,
    app_exception_handler  # type: ignore
)
app.include_router(account_router)
app.include_router(stock_router)
app.include_router(stock_list_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
