from pydantic import BaseModel


class StockListSchema(BaseModel):
    name: str
    account_id: int

    class Config:
        orm_mode = True