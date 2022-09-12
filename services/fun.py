"""from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models

def response_order(id: int, quantity: int, pizza_size: str, order_status: str,order_location):
    
    response = {
        "quantity": quantity,
        "pizzuvicorn main:appa_size": pizza_size,
        "order_status": order_status,
        "order_location":order_location
    }
    return 


def check_if_phone_already_used(user_phone: str,session:Session):
    db_phone = session.query(models.User).filter(models.User.phone==user_phone).first()

    if db_phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

def check_if_name_already_used(user_name: str, session: Session):
    db_name = session.query(models.User).filter(models.User.name==user_name).first()

    if db_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exists"
        )

def create_new_user(user_name: str, user_phone: str):
    new_user =models. User(
        name = user_name,
        Phone = user_phone,
    )        
    return new_user
def create_new_order(pizza_size: str, quantity: int, user: models.User):
    new_order = models.OrderDetails(
        pizza_size = pizza_size,
        quantity = quantity
    )
    new_order.models.User = user
    return new_orderdef find_current_user( session: Session):

    user = session.query(models.User).filter(models.User.name == current_user).first()

    return user
def find_user(user_username: str, session : Session):
    
    db_user = session.query(models.User).filter(models.User.name==user_username).first()

    return db_user"""