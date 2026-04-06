from fastapi import Depends

from app.repository import *
from app.repository.impl import *
from app.repository.stock_list_stock_repository import StockListStockRepository


def get_account_repository(
    repo: AccountRepositoryImpl = Depends(AccountRepositoryImpl),
) -> AccountRepository:
    return repo

def get_stock_list_repository(
        repo: StockListRepositoryImpl = Depends(StockListRepositoryImpl),
) -> StockListRepository:
    return repo

def get_stock_list_stock_repository(
        repo: StockListStockRepositoryImpl = Depends(StockListStockRepositoryImpl),
) -> StockListStockRepository:
    return repo