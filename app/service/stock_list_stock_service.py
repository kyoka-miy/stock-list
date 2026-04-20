from abc import ABC, abstractmethod


class StockListStockService(ABC):
    @abstractmethod
    def add_symbols_to_list(self, stock_list_id: int, symbols: list[str]):
        pass

    @abstractmethod
    def remove_symbols_from_list(self, stock_list_id: int, symbols: list[str]):
        pass

    @abstractmethod
    def get_not_registered_symbols(self, stock_list_id: int, symbols: list[str]) -> list[str]:
        pass

    @abstractmethod
    def get_symbols_by_list_id(self, stock_list_id: int) -> list[str]:
        pass

    @abstractmethod
    def delete_list(self, stock_list_id: int) -> None:
        pass
