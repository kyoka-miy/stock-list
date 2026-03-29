from pydantic import BaseModel


class StockSearchResponse(BaseModel):
    symbol: str
    name: str
    yahoo_url: str
    ir_bank_url: str
    buffett_code_url: str
    