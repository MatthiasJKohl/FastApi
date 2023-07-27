from fastapi import APIRouter, Depends
from schemas.ClientSchemas import ClientCreateRequest
from sqlalchemy.orm import Session 
from database_configs.connection import get_db
from services.ClientService import ClientService

router = APIRouter(
    prefix="/clientCreation",
    tags=["clientCreation"],
)

@router.post ("/createClient")
def create(createClientPayload: ClientCreateRequest, db: Session = Depends(get_db)):
    clientService = ClientService(db)
    createdClient = clientService.createClient(createClientPayload)
    return createdClient