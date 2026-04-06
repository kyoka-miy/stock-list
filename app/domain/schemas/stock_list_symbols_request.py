import re

from pydantic import BaseModel, field_validator

class StockListSymbolsRequest(BaseModel):
    symbols: list[str]

    @field_validator('symbols')
    @classmethod
    def validate_symbols(cls, v):
        jp_pattern = r'^\d{4}(\.T)?$'         # e.g. 7203 or 7203.T
        us_pattern = r'^[A-Z]{1,5}$'           # e.g. AAPL, MSFT
        for symbol in v:
            if not (re.match(jp_pattern, symbol) or re.match(us_pattern, symbol)):
                raise ValueError('All symbols must be valid Japanese or US stock codes')
        return v
