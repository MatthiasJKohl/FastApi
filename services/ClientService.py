from sqlalchemy.orm import Session
from sqlalchemy import func
from database_configs.models import Client
from schemas.ClientSchemas import ClientCreateRequest
from fastapi import HTTPException


class ClientService:
    def __init__(self, db:Session):
        self.db = db

    def getClientByName(self, name:str):
        return self.db.query(Client).filter(func.lower(Client.name) == name.lower()).first()

    def createClient(self, requestBody: ClientCreateRequest):
        client = self.getClientByName(requestBody.name)

        if client:
            raise HTTPException(status_code=400, detail="Error: Client already registered!")

        addedClient = Client(name=requestBody.name, gender=requestBody.gender, age=requestBody.age)

        self.db.add(addedClient)
        self.db.commit()
        self.db.refresh(addedClient)