from typing import List

from fastapi import Depends

from app.domain.models.account import Account
from app.repository.account_repository import AccountRepository
from app.dependencies import get_account_repository
from app.exceptions.app_exception import AppException


class AccountUseCase:
    def __init__(self, repository: AccountRepository = Depends(get_account_repository)):
        self.repository = repository

    def get_accounts(self) -> List[Account]:
        return self.repository.get_accounts()

    def create_account(self, account: Account) -> Account:
        return self.repository.create_account(account)
    
    def update_account(self, id: int, account: Account) -> Account:
        existing_account = self.repository.get_account_by_id(id)
        if not existing_account:
            raise AppException("Account not found")

        existing_account.name = account.name
        existing_account.email = account.email
        return self.repository.update_account(existing_account)
    
    def delete_account(self, id: int):
        existing_account = self.repository.get_account_by_id(id)
        if not existing_account:
            raise AppException("Account not found")

        self.repository.delete_account(id)
