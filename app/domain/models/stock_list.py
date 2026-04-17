from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class StockList(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
