from abc import ABC, abstractmethod
from app.domain.models.stock_list import StockList


class StockListService(ABC):
    @abstractmethod
    def get_stock_list_by_id(self, id: int) -> StockList:
        pass

    @abstractmethod
    def update_stock_list_name(self, stock_list_id: int, name: str) -> StockList:
        pass

    @abstractmethod
    def create_stock_list(self, stock_list: StockList) -> StockList:
        pass

    @abstractmethod
    def delete_list(self, stock_list_id: int) -> None:
        pass
