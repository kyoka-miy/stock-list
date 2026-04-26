import logging

from yfinance import Ticker

from app.service.stock_info_provider import StockInfoProvider


class YFinanceInfoProviderImpl(StockInfoProvider):
    logger = logging.getLogger(__name__)

    def get_valid_symbols(self, symbols: list[str]) -> list[str]:
        valid_symbols = []
        for symbol in symbols:
            ticker = Ticker(symbol)
            try:
                info = ticker.info
                if info.get("symbol") == symbol:
                    valid_symbols.append(symbol)
            except Exception:
                continue
        return valid_symbols

    def get_stock_info(self, symbol: str) -> dict | None:
        info = None
        try:
            ticker = Ticker(symbol)
            info = ticker.info
            if info.get("symbol") != symbol:
                info = None
        except Exception:
            self.logger.warning(f"Failed to fetch stock info for symbol: {symbol}", exc_info=True)

        return info