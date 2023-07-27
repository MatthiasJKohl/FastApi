from fastapi import APIRouter, Depends
from schemas.OrderSchemas import OrderCreateRequest
from sqlalchemy.orm import Session 
from database_configs.connection import get_db
from services.OrderService import OrderService

router = APIRouter(
    prefix="/foodParcels",
    tags=["foodParcelOrders"],
)

@router.post ("/foodParcels")
def order(createOrderPayload: OrderCreateRequest , db: Session = Depends(get_db)):
    orderService = OrderService(db)
    createdClient = orderService.createOrder(OrderCreateRequest)
    return createdClient