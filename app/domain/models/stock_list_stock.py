from sqlalchemy import Column, Integer, ForeignKey, String
from app.db.base_class import Base


class StockListStock(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    stock_list_id = Column(Integer, ForeignKey("stocklist.id"), nullable=False)
    symbol = Column(String, nullable=False)