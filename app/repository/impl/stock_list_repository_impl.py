
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.domain.models.stock_list import StockList
from app.repository.stock_list_repository import StockListRepository


class StockListRepositoryImpl(StockListRepository):
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_list(self, stock_list: StockList) -> StockList:
        self.db.add(stock_list)
        self.db.commit()
        self.db.refresh(stock_list)
        return stock_list

    def get_list_by_id(self, id: int) -> StockList | None:
        return self.db.query(StockList).filter(StockList.id == id).first()

    def update_list_name(self, stock_list_id: int, name: str) -> None:
        self.db.query(StockList).filter(StockList.id ==
                                        stock_list_id).update({StockList.name: name})
        self.db.commit()

    def delete_list(self, stock_list_id: int) -> None:
        self.db.query(StockList).filter(StockList.id == stock_list_id).delete()
        self.db.commit()
