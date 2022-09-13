from statistics import quantiles
from typing import Optional
from unicodedata import name
from pydantic import BaseModel, Field


class create(BaseModel): 
    name: str = Field(min_length=6,max_length=100) 
    phone : str=Field(max_length=11,min_length=11)
    

    class Config:
        orm_mode = True
       
       
       
       
        # nschema_extra = {
        #      "example":{
        #          "name":"Bakr",
        #          "phone":"015",
        #          "location":"6 of october"
                
        #    }
        # }

class createorder(BaseModel):
    phone:str =Field(max_length=11,min_length=11)
    name:str  
    quantity: int =Field(gt=0)
    order_status:str = "PENDING" 
    pizza_size: str ="Small"
    location :str
    class Config:
        orm_mode = True
       
class update(BaseModel):
    id:int
    name:Optional[str] 
    quantity:Optional[int] =Field(gt=0)
    quantity: int =Field(gt=0) 
    order_status:str = "PENDING" 
    pizza_size: str ='Small'
    location :str