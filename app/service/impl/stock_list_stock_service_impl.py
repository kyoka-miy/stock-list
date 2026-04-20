from fastapi import Depends
from app.repository.dependencies import get_stock_list_stock_repository
from app.exceptions.app_exception import AppException
from app.repository.stock_list_stock_repository import StockListStockRepository
from ..stock_list_stock_service import StockListStockService


class StockListStockServiceImpl(StockListStockService):
    def __init__(self, repository: StockListStockRepository = Depends(get_stock_list_stock_repository)):
        self.repository = repository

    def add_symbols_to_list(self, stock_list_id: int, symbols: list[str]):
        self.repository.add_symbols_to_list(stock_list_id, symbols)

    def remove_symbols_from_list(self, stock_list_id: int, symbols: list[str]):
        self.repository.remove_symbols_from_list(stock_list_id, symbols)

    def get_not_registered_symbols(self, stock_list_id: int, symbols: list[str]) -> list[str]:
        symbols_in_list = set(
            self.repository.get_symbols_by_stock_list_id(stock_list_id))
        not_registered_symbols = [
            symbol for symbol in symbols if symbol not in symbols_in_list]
        if not not_registered_symbols:
            raise AppException(
                "All symbols are already registered in the list")
        return not_registered_symbols

    def get_symbols_by_list_id(self, stock_list_id: int) -> list[str]:
        return self.repository.get_symbols_by_stock_list_id(stock_list_id)

    def delete_list(self, stock_list_id: int) -> None:
        self.repository.remove_list(stock_list_id)
