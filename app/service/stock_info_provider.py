from abc import ABC, abstractmethod


class StockInfoProvider(ABC):
    @abstractmethod
    def get_valid_symbols(self, symbols: list[str]) -> list[str]:
        pass

    @abstractmethod
    def get_stock_info(self, symbol: str) -> dict | None:
        pass