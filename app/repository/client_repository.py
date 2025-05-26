from sqlmodel import Session, select
from app.models.client import Client

class ClientRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, client_id: int) -> Client | None:
        statement = select(Client).where(Client.id == client_id)
        return self.session.exec(statement).first()

    def get_all(self) -> list[Client]:
        statement = select(Client)
        return list(self.session.exec(statement))

