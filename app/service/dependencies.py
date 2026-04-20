from fastapi import Depends

from app.service import *
from app.service.impl import *


def get_stock_list_service(
        service: StockListServiceImpl = Depends(StockListServiceImpl),
) -> StockListService:
    return service

def get_stock_list_stock_service(
        service: StockListStockServiceImpl = Depends(StockListStockServiceImpl),
) -> StockListStockService:
    return service