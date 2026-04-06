from typing import List, Optional

from app.db.session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

from app.domain.models.account import Account
from app.repository.account_repository import AccountRepository
from app.exceptions.app_exception import AppException
from sqlalchemy.exc import IntegrityError


class AccountRepositoryImpl(AccountRepository):
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_accounts(self) -> List[Account]:
        return self.db.query(Account).all()

    def create_account(self, account: Account) -> Account:
        try:
            self.db.add(account)
            self.db.commit()
            self.db.refresh(account)
            return account

        except IntegrityError as e:
            self.db.rollback()
            raise AppException("Email already exists") from e
        
    def get_account_by_id(self, id: int) -> Optional[Account]:
        return self.db.query(Account).filter(Account.id == id).first()
    
    def update_account(self, account: Account) -> Account:
        try:
            self.db.merge(account)
            self.db.commit()
            self.db.refresh(account)
            return account

        except IntegrityError as e:
            self.db.rollback()
            raise AppException("Email already exists") from e
        
    def delete_account(self, id: int):
        account = self.db.query(Account).filter(Account.id == id).first()
        self.db.delete(account)
        self.db.commit()
