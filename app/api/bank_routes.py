from fastapi import APIRouter, Depends
from app.services.bank_service import TransferService
from app.api.dependencies import get_transfer_service

router = APIRouter()

@router.post("/bank/transfer")
def transfer_money_online(from_account_id: int, to_account_id: int, amount: int,
                         transfer_service: TransferService = Depends(get_transfer_service)):
    """
    Transfer money online between two accounts
    """
    transfer_service.transfer_money(from_account_id, to_account_id, amount)
    return {"message": "Transfer successful"}
