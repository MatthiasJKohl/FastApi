from pydantic import BaseModel, validator
from typing import Optional 


class ClientCreateRequest(BaseModel):
    name : str
    gender : str
    age : str

    @validator('name')
    def validate_name(cls, v):

        if len(v) == 0:
            raise ValueError('Error: Name cannot be blank!')

        if not v.replace(' ', '').isalpha():
            raise ValueError('Error: Name can only include alphabetical characters!')
        
        if len(v) > 50:
            raise ValueError('Error: Name must be less than 50 characters!')
        
        if len(v) < 4:
            raise ValueError('Error: Name must be atleast 4 characters!')
        

        return v.strip()

class ClientResponseModel(BaseModel):
    name : str
    gender : str
    age : str


    class Config:
        orm_mode = True 