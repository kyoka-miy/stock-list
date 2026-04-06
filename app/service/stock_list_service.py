from fastapi import Depends

from app.dependencies import get_stock_list_repository
from app.domain.models.stock_list import StockList
from app.exceptions.app_exception import AppException
from app.repository.stock_list_repository import StockListRepository


class StockListService:
    def __init__(
            self,
            stock_list_repository: StockListRepository = Depends(get_stock_list_repository)):
        self.repository = stock_list_repository

    def get_stock_list_by_id(self, id: int) -> StockList | None:
        return self.repository.get_list_by_id(id)

    def update_stock_list_name(self, stock_list_id: int, name: str) -> StockList:
        return self.repository.update_list_name(stock_list_id, name)

    def create_stock_list(self, stock_list: StockList) -> StockList:
        return self.repository.create_list(stock_list)

    def delete_list(self, stock_list_id: int) -> None:
        self.repository.delete_list(stock_list_id)
