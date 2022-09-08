from typing import Optional
from unicodedata import name
from pydantic import BaseModel


class SignUpModel(BaseModel):
    name: str
    phone: str

    class Config:
        orm_mode = True
        nschema_extra = {
             "example":{
                 "name":"Bakr",
                 "phone":"015"
                
           }
        }

class OrderModel(BaseModel):
   # id: Optional[int]
    quantity: int
    name:str 
    order_status:str = "PENDING" 
    pizza_size: str = "SMALL"

    class Config:
        orm_mode = True
        class Config:
           orm_mode = True
           schema_extra = {
            "example":{
                "quantity": 2,
                "pizza_size": "LARGE"
            }
        }
class create_order_user(BaseModel):
     name:str