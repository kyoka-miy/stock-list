from fastapi import APIRouter, Depends
import yfinance

from app.usecase.stock_usecase import StockUseCase
from app.domain.schemas.stock_search_response import StockSearchResponse

router = APIRouter(tags=["Stocks"], prefix="/stocks")


@router.get("/search", response_model=list[StockSearchResponse])
def search_stocks(q: str, usecase: StockUseCase = Depends()):
    return usecase.search_stocks(q)
