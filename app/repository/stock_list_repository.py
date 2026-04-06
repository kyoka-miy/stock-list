from abc import ABC, abstractmethod

from app.domain.models.stock_list import StockList


class StockListRepository(ABC):
    @abstractmethod
    def create_list(self, stock_list: StockList) -> StockList:
        pass

    @abstractmethod
    def get_list_by_id(self, id: int) -> StockList | None:
        pass

    @abstractmethod
    def update_list_name(self, stock_list_id: int, name: str) -> StockList:
        pass

    @abstractmethod
    def delete_list(self, stock_list_id: int) -> None:
        pass
