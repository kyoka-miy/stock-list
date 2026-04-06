from fastapi import APIRouter, Depends

from app.domain.schemas.account_schema import AccountSchema
from app.domain.models.account import Account
from app.usecase.account_usecase import AccountUseCase


router = APIRouter(tags=["Accounts"], prefix="/accounts")


@router.get("/", response_model=list[AccountSchema])
def get_accounts(usecase: AccountUseCase = Depends(AccountUseCase)):
    return usecase.get_accounts()

@router.post("/", response_model=AccountSchema)
def create_account(account: AccountSchema, usecase: AccountUseCase = Depends(AccountUseCase)):
    return usecase.create_account(Account(**account.model_dump()))

# TODO: use context
@router.put("/{id}", response_model=AccountSchema)
def update_account(id: int, account: AccountSchema, usecase: AccountUseCase = Depends(AccountUseCase)):
    return usecase.update_account(id, Account(**account.model_dump()))

@router.delete("/{id}")
def delete_account(id: int, usecase: AccountUseCase = Depends(AccountUseCase)):
    usecase.delete_account(id)
    return {"message": "Account deleted successfully"}