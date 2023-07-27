from pydantic import BaseModel, validator
from typing import Optional 


class OrderCreateRequest(BaseModel):
    data_given : str
    client_id : int
    parcel_id : int



class OrderResponseModel(BaseModel):
    date_given : str
    client_id : int
    parcel_id : int


    class Config:
        orm_mode = True
