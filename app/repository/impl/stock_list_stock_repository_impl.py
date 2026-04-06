from fastapi import Depends
from app.repository.stock_list_stock_repository import StockListStockRepository
from app.domain.models.stock_list_stock import StockListStock
from app.db.session import get_db
from sqlalchemy.orm import Session


class StockListStockRepositoryImpl(StockListStockRepository):
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def add_symbols_to_list(self, stock_list_id: int, symbols: list[str]) -> None:
        objects = [StockListStock(
            stock_list_id=stock_list_id, symbol=symbol) for symbol in symbols]  # type: ignore
        self.db.bulk_save_objects(objects)
        self.db.commit()

    def remove_symbols_from_list(self, stock_list_id: int, symbols: list[str]) -> None:
        self.db.query(StockListStock).filter(
            StockListStock.stock_list_id == stock_list_id,
            StockListStock.symbol.in_(symbols)
        ).delete(synchronize_session=False)
        self.db.commit()

    def get_symbols_by_stock_list_id(self, stock_list_id: int) -> list[str]:
        rows = self.db.query(StockListStock.symbol).filter_by(
            stock_list_id=stock_list_id).all()
        return [row[0] for row in rows]

    def remove_list(self, stock_list_id: int) -> None:
        self.db.query(StockListStock).filter(
            StockListStock.stock_list_id == stock_list_id
        ).delete(synchronize_session=False)
        self.db.commit()
