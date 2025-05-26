from sqlmodel import SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .account import Account

class Client(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    national_id: str = Field(index=True, unique=True)
    name: str
    accounts: List["Account"] = Relationship(back_populates="client")
