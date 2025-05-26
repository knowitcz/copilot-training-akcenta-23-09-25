from app.repository.client_repository import ClientRepository
from app.models.client import Client

class ClientService:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def get_client_by_id(self, client_id: int) -> Client | None:
        return self.client_repository.get_by_id(client_id)

    def get_all_clients(self) -> list[Client]:
        return self.client_repository.get_all()
