from fastapi import Depends

from app.domain.models.stock_list import StockList
from app.exceptions.app_exception import AppException
from app.service.stock_list_service import StockListService
from app.service.stock_list_stock_service import StockListStockService


class StockListUseCase:
    def __init__(
            self,
            stock_list_service: StockListService = Depends(StockListService),
            stock_list_stock_service: StockListStockService = Depends(StockListStockService)):
        self.stock_list_service = stock_list_service
        self.stock_list_stock_service = stock_list_stock_service

    def create_stock_list(self, stock_list: StockList) -> StockList:
        return self.stock_list_service.create_stock_list(stock_list)

    def update_stock_list(self, stock_list_id: int, name: str) -> StockList:
        self._exists_stock_list_by_id(stock_list_id)

        return self.stock_list_service.update_stock_list_name(stock_list_id, name)

    def add_symbols_to_list(self, stock_list_id: int, symbols: list[str]) -> None:
        self._exists_stock_list_by_id(stock_list_id)

        not_registered_symbols = self.stock_list_stock_service.get_not_registered_symbols(
            stock_list_id, symbols)

        if (not not_registered_symbols):
            raise AppException(
                "All symbols are already registered in the list")

        self.stock_list_stock_service.add_symbols_to_list(
            stock_list_id, not_registered_symbols)

    def remove_symbols_from_list(self, stock_list_id: int, symbols: list[str]) -> None:
        self._exists_stock_list_by_id(stock_list_id)

        self.stock_list_stock_service.remove_symbols_from_list(
            stock_list_id, symbols)

    def delete_list(self, stock_list_id: int) -> None:
        self._exists_stock_list_by_id(stock_list_id)

        # Delete all related records from stock_list_stock first
        self.stock_list_stock_service.delete_list(
            stock_list_id)

        # Then delete the stock list itself
        self.stock_list_service.delete_list(stock_list_id)

    def _exists_stock_list_by_id(self, stock_list_id):
        stock_list = self.stock_list_service.get_stock_list_by_id(
            stock_list_id)
        if not stock_list:
            raise AppException("Stock list not found")
