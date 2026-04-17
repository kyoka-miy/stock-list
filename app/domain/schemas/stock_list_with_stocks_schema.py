from typing import Any

from pydantic import BaseModel


from pydantic import BaseModel


class StockInfoSchema(BaseModel):
    symbol: str
    name: str
    current_price: float | None
    dividend_yield: float | None
    dividend_per_share: float | None
    payout_ratio: float | None
    per: float | None
    pbr: float | None
    roe: float | None
    roa: float | None
    market: str | None
    sector: str | None
    industry: str | None


class StockListWithStocksSchema(BaseModel):
    name: str
    stocks: list[StockInfoSchema]
