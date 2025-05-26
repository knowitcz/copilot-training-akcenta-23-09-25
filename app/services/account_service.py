from app.models.account import Account
from app.models.transaction import Transaction
from app.repository.account_repository import AccountRepository
from app.repository.transaction_repository import TransactionRepository
from datetime import datetime


class AccountService(object):
    def __init__(self, account_repository: AccountRepository, transaction_repository: TransactionRepository):
        self.account_repository = account_repository
        self.transaction_repository = transaction_repository

    def get_account_by_id(self, account_id: int) -> Account | None:
        """
        Get account by ID
        """
        return self.account_repository.get_by_id(account_id)

    def transfer_money(self, from_account_id: int, to_account_id: int, amount: int) -> None:
        """
        Transfer money from one account to another within a single transaction
        """
        with self.account_repository.session.begin():
            self.account_repository.withdraw_money(from_account_id, amount)
            self.account_repository.deposit_money(to_account_id, amount)
            self.transaction_repository.add(amount, from_account_id=from_account_id, to_account_id=to_account_id)

    def withdraw_money(self, account_id: int, amount: int) -> None:
        """
        Withdraw money from an account
        """
        with self.account_repository.session.begin():
            self.account_repository.withdraw_money(account_id, amount)
            self.transaction_repository.add(amount, from_account_id=account_id)

    def deposit_money(self, account_id: int, amount: int) -> None:
        """
        Deposit money into an account
        """
        with self.account_repository.session.begin():
            self.account_repository.deposit_money(account_id, amount)
            self.transaction_repository.add(amount, to_account_id=account_id)
