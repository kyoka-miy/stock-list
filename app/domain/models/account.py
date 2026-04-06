from datetime import datetime
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Integer

class Account(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)