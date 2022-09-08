from hashlib import new
from xml.sax import default_parser_list
from fastapi import FastAPI , Depends, HTTPException, status
from regex import F
from database import engine,SessionLocal 
from fun import (find_user,create_new_user,check_if_phone_already_used,check_if_name_already_used,create_new_order)
import models, schemas
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post('/create_user',status_code=status.HTTP_201_CREATED)
def create_user(user:schemas.SignUpModel,db: Session = Depends(get_db)):
    check_if_phone_already_used(models.user.phone, Session= Depends(get_db))

    check_if_name_already_used(user.username, Session= Depends(get_db))

    new_user =create_new_user(models.user.name,models. user.phone)

    db.Session.add(new_user)
    db.Session.commit()
    db.refresh(new_user)
    return {'message':'Success! You\'ve just signed up!'}





@app.post('/creat_order')
def create_order(order:schemas.OrderModel,user:schemas.create_order_user,db:Session = Depends(get_db)):
    user_find= find_user(models.User.name,Session = Depends(get_db))
    if not user_find:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid Username or Password")
    new_order =create_new_order(models.order.pizza_size,models.order.quantitiy)
    Session.add(new_order)
    Session.commit()
    return {'message':'order created'}
@app.get('/get_order/{id}')
def get_order(id:int,db:Session =Depends(get_db)):
    order = Session.query(models.Order).filter(models.Order.id == id).first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order with the given ID doesn't exist"
        )
    
    return order
@app.put('/update_order/{id}')
def update(id:int,Session=Depends(get_db)):
    order_to_update= Session.query(models.Order).filter(models.Order.id == id).first()
    #user = session.query(User).filter(User.username == current_user).first()
    if not order_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order with the given ID doesn't exist"
        )

    order_to_update.quantity = models.Order.quantity
    order_to_update.pizza_size =models.models. Order.pizza_size

    Session.commit()

    return order_to_update
        

