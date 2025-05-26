from fastapi import Depends
from sqlmodel import Session
from app.db import get_session
from app.repository.account_repository import AccountRepository
from app.services.account_service import AccountService
from app.services.bank_service import OnlineBankService, TransferService
from app.validator.amount_validator import AmountValidatorProtocol, positive_amount_validator
from app.repository.client_repository import ClientRepository
from app.services.client_service import ClientService

def get_account_service(session: Session = Depends(get_session)) -> AccountService:
    repo = AccountRepository(session)
    return AccountService(repo)

def get_transfer_service(account_service: AccountService = Depends(get_account_service)) -> TransferService:
    amount_validator: AmountValidatorProtocol = positive_amount_validator
    return OnlineBankService(account_service, amount_validator)

def get_client_service(session: Session = Depends(get_session)) -> ClientService:
    repo = ClientRepository(session)
    return ClientService(repo)
