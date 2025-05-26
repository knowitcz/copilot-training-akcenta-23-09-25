from sqlmodel import SQLModel, Field
from datetime import datetime

class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    from_account_id: int | None = Field(default=None, foreign_key="account.id")
    to_account_id: int | None = Field(default=None, foreign_key="account.id")
    amount: int
    timestamp: datetime = Field(default_factory=datetime.utcnow, nullable=False)
