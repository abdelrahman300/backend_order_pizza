from typing import Optional
from unicodedata import name
from pydantic import BaseModel


class SignUpModel(BaseModel):
    id: Optional[int]
    name: str
    phone: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example":{
                "name":"Bakr",
                "phone":"015"
                
            }
        }

class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    name:str 
    order_status: Optional[str] = "PENDING" 
    pizza_size: str = "SMALL"
    user_id:int

    class Config:
        orm_mode = True
        schema_extra = {
            "example":{
                "quantity": 2,
                "pizza_size": "LARGE"
            }
        }

class OrderStatusModel(BaseModel):
    order_status: Optional[str] = "PENDING"

    class Config:
        orm_mode = True
        schema_extra = {
            "example":{
                "order_status":"PENDING"
            }
        }
class create_order_user(BaseModel):
    name:str