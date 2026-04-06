from pydantic import BaseModel, field_validator


class StockListNameRequest(BaseModel):
    name: str
