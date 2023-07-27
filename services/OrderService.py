from sqlalchemy.orm import Session
from sqlalchemy import func
from database_configs.models import FoodParcelOrders
from schemas.OrderSchemas import OrderCreateRequest
from fastapi import HTTPException


class OrderService:
    def __init__(self, db:Session):
        self.db = db

    def createOrder(self, requestBody: OrderCreateRequest):
        
        orderCreated = FoodParcelOrders(date_given=requestBody.data_given, client_id=requestBody.client_id, parcel_id=requestBody.parcel_id)

        self.db.add(orderCreated)
        self.db.commit()
        self.db.refresh(orderCreated)