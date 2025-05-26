from datetime import datetime
from sqlmodel import Session, SQLModel
from app.repository.transaction_repository import TransactionRepository

class TransactionSummary(SQLModel):
    client_id: int
    incoming_sum: int
    outgoing_sum: int

class StatisticsService:
    def __init__(self, session: Session):
        self.session = session
        self.transaction_repo = TransactionRepository(session)

    def transaction_summary(self, client_id: int, start: datetime, end: datetime) -> TransactionSummary:
        """
        Compute the sum of all incoming and outgoing money transfers for a specified client and time interval.
        """
        incoming_sum = self.transaction_repo.get_incoming_sum_by_client(client_id, start, end)
        outgoing_sum = self.transaction_repo.get_outgoing_sum_by_client(client_id, start, end)

        return TransactionSummary(
            client_id=client_id,
            incoming_sum=incoming_sum,
            outgoing_sum=outgoing_sum
        )
