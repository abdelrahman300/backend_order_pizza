from typing import Optional
from unicodedata import name
from pydantic import BaseModel, Field


class SignUpModel(BaseModel):
    name: str = Field(min_length=6,max_length=100) 
    phone: str=Field(max_length=11,min_length=11)
    

    class Config:
        orm_mode = True
        # nschema_extra = {
        #      "example":{
        #          "name":"Bakr",
        #          "phone":"015",
        #          "location":"6 of october"
                
        #    }
        # }

class OrderModel(BaseModel):
    name:str
    quantity: int 
    order_status:str = "PENDING" 
    pizza_size: str = "SMALL"
    location :str

    class Config:
        orm_mode = True
        # class Config:
        #    orm_mode = True
        #    schema_extra = {
        #     "example":{
        #         "quantity": 2,
        #         "pizza_size": "LARGE"
        #     }
        # }
class create_order_user(BaseModel):
      phone:str =Field(max_length=11,min_length=11)