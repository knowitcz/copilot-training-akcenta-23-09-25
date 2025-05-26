from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .client import Client

class Account(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    balance: int
    type: str
    client_id: int = Field(foreign_key="client.id")
    # Relationship to Client
    client: "Client" = Relationship(back_populates="accounts")
