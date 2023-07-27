from fastapi import FastAPI, Depends, HTTPException
from clients_logic.ClientService import ClientService
from database_configs.connection import Base,engine, get_db
from database_configs import models
from sqlalchemy.orm import Session 

from schemas.ClientSchemas import ClientCreateRequest, ClientResponseModel

from origins import origins
from fastapi.middleware.cors import CORSMiddleware

from routes.clientCreation import router as clientRouter


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clientRouter)


@app.get("/")
def home():
    return {"message": "Hello World"}

# @app.get("/clients")
# def getAllClients():
#     clientService = ClientService()
#     return clientService.getAllClients()

@app.get("/clients")
def get_all_clients(db: Session = Depends(get_db)):
    clients = db.query(models.Client).all()
    return clients

@app.post("/clients", response_model=ClientResponseModel)
def createClient(clientRequestBody: ClientCreateRequest, db: Session = Depends(get_db)):
    client = models.Client(name=clientRequestBody.name, gender=clientRequestBody.gender, age=clientRequestBody.age)
    
    db.add(client)

    db.commit()

    db.refresh(client)

    return client



