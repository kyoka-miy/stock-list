from fastapi import Depends

from app.repository.account_repository import AccountRepository
from app.repository.impl.account_repository_impl import AccountRepositoryImpl


def get_account_repository(
    repo: AccountRepositoryImpl = Depends(AccountRepositoryImpl),
) -> AccountRepository:
    return repo