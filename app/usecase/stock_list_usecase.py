import pprint

from fastapi import Depends

from app.domain.models.stock_list import StockList
from app.domain.schemas.page_schema import PageSchema
from app.domain.schemas.stock_list_with_stocks_schema import StockListWithStocksSchema, StockInfoSchema
from app.exceptions.app_exception import AppException
from app.service.dependencies import get_stock_list_service, get_stock_list_stock_service
from app.service.impl.stock_list_service_impl import StockListService
from app.service.impl.stock_list_stock_service_impl import StockListStockService
from yfinance import Ticker


class StockListUseCase:
    def __init__(
            self,
            stock_list_service: StockListService = Depends(
                get_stock_list_service),
            stock_list_stock_service: StockListStockService = Depends(get_stock_list_stock_service)):
        self.stock_list_service = stock_list_service
        self.stock_list_stock_service = stock_list_stock_service

    def create_stock_list(self, stock_list: StockList) -> StockList:
        return self.stock_list_service.create_stock_list(stock_list)

    def update_stock_list(self, stock_list_id: int, name: str) -> StockList:
        self.stock_list_service.get_stock_list_by_id(
            stock_list_id)

        return self.stock_list_service.update_stock_list_name(stock_list_id, name)

    def add_symbols_to_list(self, stock_list_id: int, symbols: list[str]) -> None:
        self.stock_list_service.get_stock_list_by_id(stock_list_id)

        not_registered_symbols = self.stock_list_stock_service.get_not_registered_symbols(
            stock_list_id, symbols)

        # get valid symbols by yfinance
        valid_symbols = []
        for symbol in not_registered_symbols:
            try:
                ticker = Ticker(symbol)
                info = ticker.info
                if info.get("symbol") == symbol:
                    valid_symbols.append(symbol)
            except Exception:
                raise AppException(
                    f"Failed to fetch data for symbol: {symbol}")

        self.stock_list_stock_service.add_symbols_to_list(
            stock_list_id, valid_symbols)

    def remove_symbols_from_list(self, stock_list_id: int, symbols: list[str]) -> None:
        self.stock_list_service.get_stock_list_by_id(stock_list_id)

        self.stock_list_stock_service.remove_symbols_from_list(
            stock_list_id, symbols)

    def delete_list(self, stock_list_id: int) -> None:
        self.stock_list_service.get_stock_list_by_id(stock_list_id)

        # Delete all related records from stock_list_stock first
        self.stock_list_stock_service.delete_list(
            stock_list_id)

        # Then delete the stock list itself
        self.stock_list_service.delete_list(stock_list_id)


# TODO: sort, pagenation, cache

    def get_stock_list_with_indicators(self, stock_list_id: int, pageSize: int = 20, pageNumber: int = 1) -> StockListWithStocksSchema:
        stock_list = self.stock_list_service.get_stock_list_by_id(
            stock_list_id)

        symbols = self.stock_list_stock_service.get_symbols_by_list_id(
            stock_list_id)
        stocks: list[StockInfoSchema] = []
        for symbol in symbols:
            try:
                ticker = Ticker(symbol)
                info = ticker.info
                if info.get("symbol") != symbol:
                    continue
            except Exception:
                raise AppException(
                    f"Failed to fetch data for symbol: {symbol}")
            pprint.pprint(info)

            stocks.append(StockInfoSchema(
                symbol=symbol,
                name=info.get("longName") or info.get("shortName") or "",
                current_price=info.get("currentPrice"),
                dividend_yield=info.get("dividendYield"),  # 配当利回り
                dividend_per_share=info.get("dividendRate"),  # 1株あたりの配当金
                payout_ratio=self._get_percent_and_round(
                    info.get("payoutRatio")),  # 配当性向
                per=self._get_round(info.get("trailingPE")),
                pbr=self._get_round(info.get("priceToBook")),
                roe=self._get_percent_and_round(info.get("returnOnEquity")),
                roa=self._get_percent_and_round(info.get("returnOnAssets")),
                market=info.get("exchange"),
                sector=info.get("sector"),
                industry=info.get("industry")
            ))
        return StockListWithStocksSchema(
            name=stock_list.name,
            stocks=PageSchema(
                pageNumber=pageNumber,
                pageSize=pageSize,
                items=stocks
            )
        )

    def _get_percent_and_round(self, val):
        if isinstance(val, (int, float)):
            return round(val * 100, 2)
        return None

    def _get_round(self, val):
        if isinstance(val, (int, float)):
            return round(val, 2)
        return None
