from hashlib import new
from fastapi.responses import JSONResponse
from sqlite3 import dbapi2
from xml.sax import default_parser_list
from fastapi import FastAPI , Depends, HTTPException, status
from regex import F
from database import engine,SessionLocal 
import models
from .schemas import (SignUpModel )
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/create/user',status_code=status.HTTP_201_CREATED)
def create_user(user:SignUpModel,db: Session = Depends(get_db)):
    user_phone = db.query(models.User).filter(models.User.phone==user.phone).first()
    if  user_phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    user_name = db.query(models.User).filter(models.User.name==user.name).first()

    if user_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exists"
        )


    new_user = models.User(
        name = user.name,
        Phone = user.phone,
    )   

    db.add(new_user)
    db.commit()
    return {'user':new_user}


@app.post('/creat/order',status_code=status.HTTP_404_NOT_FOUND)
def create_order(order:schemas.OrderModel,user:schemas.create_order_user,db:Session = Depends(get_db)):
    user_find= db.query(models.User ).filter(models.User.id).first()
    if not user_find:
        raise HTTPException(status_code=404, detail="Item not found")
    new_order = models.OrderDetails(
        pizza_size = order.pizza_size,
        quantity = order.quantity
    )
    db.Session.add(new_order)
    db.Session.commit()
    db.refresh(new_order)
    return  JSONResponse(content=order, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
@app.get('/get_order/{id}',status_code=status.HTTP_404_NOT_FOUND)
def get_order(id:int,db:Session =Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == id).first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order with the given ID doesn't exist"
        )
    
    return order
@app.put('/update_order/{id}')
def update(id:int,db: Session = Depends(get_db)):
    order_to_update=db.query(models.Order).filter(models.Order.id == id).first()
    order_status = db.query(models.Order).filter(models.OrderDetails.ORDER_STATUSES)
    if order_status =='IN-TRANSIT':
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order Done")
        
    if not order_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order with the given ID doesn't exist"
        )

    order_to_update.quantity = models.OrderDetails.quantity
    order_to_update.pizza_size =models.OrderDetails.pizza_size
    db.add(order_to_update.quantity, order_to_update.pizza_size)
    db.Session.commit()
    db.Session.refresh(order_to_update.quantity, order_to_update.pizza_size)

    return order_to_update
        
@app.delete('/delete')
def Delete_order(id:int,db: Session = Depends(get_db)):
    del_order= db.query(models.Order).filter(models.Order.id == id).first()
    order_status = db.query(models.Order).filter(models.OrderDetails.ORDER_STATUSES)
    if order_status =='IN-TRANSIT':
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order Done"
        )
    if not del_order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order with the given ID doesn't exist"
        )
    db.Session.delete(del_order)
    db.Session.commit()   
    return 'Your order has deleted'
@app.get('/all')
def list_all_orders(db:Session = Depends(get_db)):

    orders = db.query(models.OrderDetails).all()

    if not orders:
        return {"message":"No orders were made yet"}

    return orders