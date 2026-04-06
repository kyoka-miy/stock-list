from abc import ABC, abstractmethod


class StockListStockRepository(ABC):
    @abstractmethod
    def add_symbols_to_list(self, stock_list_id: int, symbols: list[str]) -> None:
        pass

    @abstractmethod
    def remove_symbols_from_list(self, stock_list_id: int, symbols: list[str]) -> None:
        pass

    @abstractmethod
    def get_symbols_by_stock_list_id(self, stock_list_id: int) -> list[str]:
        pass

    @abstractmethod
    def remove_list(self, stock_list_id: int) -> None:
        pass
