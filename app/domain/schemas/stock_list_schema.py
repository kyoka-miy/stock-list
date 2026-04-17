from pydantic import BaseModel


class StockListSchema(BaseModel):
    name: str
    # TODO: Delete account_id
    account_id: int

    class Config:
        orm_mode = True