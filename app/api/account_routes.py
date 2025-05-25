from fastapi import APIRouter, Depends, HTTPException
from app.api.dependencies import get_account_service
from app.models.account import Account
from app.services.account_service import AccountService

router = APIRouter()

@router.get("/account/{id}", response_model=Account)
def get_account(id: int,
                account_service: AccountService = Depends(get_account_service)):
    if account := account_service.get_account_by_id(id):
        return account
    raise HTTPException(status_code=404, detail="Account not found")

@router.post("/account/withdraw")
def withdraw_money(account_id: int, amount: int,
                account_service: AccountService = Depends(get_account_service)):
    """
    Withdraw money from an account
    """
    account_service.withdraw_money(account_id, amount)
    return {"message": "Withdrawal successful"}
