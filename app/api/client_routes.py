from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import SQLModel
from app.api.dependencies import get_client_service
from app.models.client import Client
from app.services.client_service import ClientService
from typing import List

router = APIRouter()

class AccountRead(SQLModel):
    id: int
    name: str
    balance: int
    type: str


class ClientRead(SQLModel):
    id: int
    name: str
    national_id: str
    accounts: List[AccountRead]

    class Config:
        from_attributes = True


@router.get("/clients/{id}", response_model=ClientRead)
def get_client(id: int, client_service: ClientService = Depends(get_client_service)):
    """
    Get a client by ID including their accounts
    """
    if client := client_service.get_client_by_id(id):
        return client
    raise HTTPException(status_code=404, detail="Client not found")

@router.get("/clients", response_model=List[Client])
def list_clients(client_service: ClientService = Depends(get_client_service)):
    """
    List all clients
    """
    return client_service.get_all_clients()
