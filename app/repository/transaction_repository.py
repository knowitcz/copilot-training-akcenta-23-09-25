from sqlmodel import Session, select
from app.models.transaction import Transaction
from typing import List
from datetime import datetime

class TransactionRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, amount: int, *, from_account_id: int = None, to_account_id: int = None) -> None:
        transaction = Transaction(
            from_account_id=from_account_id,
            to_account_id=to_account_id,
            amount=amount,
            timestamp=datetime.utcnow()
        )
        self.session.add(transaction)

    def get_by_id(self, transaction_id: int) -> Transaction | None:
        statement = select(Transaction).where(Transaction.id == transaction_id)
        return self.session.exec(statement).first()

    def get_all(self) -> List[Transaction]:
        statement = select(Transaction)
        return list(self.session.exec(statement))

    def get_by_account(self, account_id: int) -> List[Transaction]:
        statement = select(Transaction).where(
            (Transaction.from_account_id == account_id) |
            (Transaction.to_account_id == account_id)
        )
        return list(self.session.exec(statement))
