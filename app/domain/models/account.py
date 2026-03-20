from datetime import datetime
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Integer

class Account(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)