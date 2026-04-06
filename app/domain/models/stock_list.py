from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.base_class import Base

class StockList(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    account_id = Column(Integer, ForeignKey("account.id"), nullable=False)
