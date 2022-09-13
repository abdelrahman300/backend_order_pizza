import enum
from gettext import find
from hashlib import new
from lib2to3.pgen2.token import NAME
from re import X
import re
from webbrowser import get
from fastapi.encoders import jsonable_encoder
from socket import fromfd
from fastapi.responses import JSONResponse
from sqlite3 import dbapi2
from xml.sax import default_parser_list
from fastapi import Body, FastAPI , Depends, HTTPException, Query, status,Form
#from regex import F
from database.database import engine,SessionLocal 
from database.models import *
from database.schemas import *
from sqlalchemy.orm import Session
import sys
#from fastapi.encoders import jsonable_encoder
Base.metadata.create_all(engine)

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#create user
@app.post('/create/user',status_code=status.HTTP_201_CREATED)
def create_user(add_user:create , db: Session = Depends(get_db)):
        try:   
                user_phone = db.query(user).filter(user.phone ==add_user.phone ).first()
                if  user_phone:
                        raise HTTPException(
                            status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User with this phone already exists"
                        )
                user_name = db.query(user).filter(user.name==add_user.name).first()
                if user_name:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="User with this name already exists"
                        )
                new_user = user()
                new_user.name= add_user.name
                new_user.phone  = add_user.phone  
                db.add(new_user)
                db.commit()
                
                return {'detail':'Your acoount created',
                'Your_id':new_user.id}
        except Exception as err:
            return {'name':str(err),'Descritption':sys.exc_info()[1]}







#Create order

@app.post('/creat/order',status_code=status.HTTP_201_CREATED)
def create_order(order:createorder,db:Session = Depends(get_db)):
    try:
            new_user= db.query(user).filter(order.phone==user.phone).first()
            if  not new_user:
               raise HTTPException(status_code=404, detail="You have to create account")
            new_order = orderDetails()
            new_order.name=order.name
            new_order.quantity = order.quantity
            new_order.order_status=order.order_status
            new_order.pizza_size = order. pizza_size
            new_order.location=order.location
            new_order.Owner_id=new_user.id

            db.add(new_order)
            db.commit()
            return {"message":f"your order created"}
    except Exception as err:
            return {'name':str(err),'Descritption':sys.exc_info()[1]}


# # #to get order by id
@app.get('/get_order/{id}')
def get_order(id:int,db:Session =Depends(get_db)):
    try:
        find_order = db.query(orderDetails).filter(orderDetails.id == id).first()
        if not find_order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Order with the given iD{id} doesn't exist"
            )
        return find_order
    except Exception as err:
        return {'name':str(err),'Descritption':sys.exc_info()[1]}
 
# # #get all orders/
@app.get('/all/users')
def list_all_orders(db:Session = Depends(get_db)):
    try:
        users = db.query(user).all()
        if not users:
            return {"message":"No users"}
        return users
    except Exception as err:
            return {'name':str(err),'Descritption':sys.exc_info()[1]}


@app.get('/number/of/orders')
def list_all_orders(db:Session = Depends(get_db)):
    try:
        view_orders = db.query(orderDetails).count()
        if not view_orders:
            return {"message":"No orders"}
        return view_orders
    except Exception as err:
            return {'name':str(err),'Descritption':sys.exc_info()[1]}

@app.get('/all/orders')
def list_all_orders(db:Session = Depends(get_db)):
    try:
        orders = db.query(orderDetails).all()
        if not orders:
            return {"message":"No orders"}
        return orders
    except Exception as err:
            return {'name':str(err),'Descritption':sys.exc_info()[1]}







@app.put('/update_order/{id}')
def update(id:int,new:update,db: Session = Depends(get_db)):
    try:
        order_update=db.query(orderDetails).filter(orderDetails.id==id)
        if not order_update:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Order with the given ID{id} doesn't exist"
            )
       
        order_status = db.query(orderDetails).filter(orderDetails.order_status)
        if  order_status == 'PENDING':
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Sorry ,Your order has Done"
        )    
       
        order_update.quantity =new.quantity
        order_update.pizza_size =new.pizza_size
        order_update.name=new.name
        order_update.order_status=new.order_status
        order_update.location=new.location
        order_update.update(new.dict())
        db.commit()
        return {'message ':'Update has Done'}
        
    except Exception as err:
            return {'name':str(err),'Descritption':sys.exc_info()[1]}    




@app.delete('/delete/{id}')
def Delete_order(id:int,db: Session = Depends(get_db)):
        try:   
            del_order=  db.query(orderDetails).filter(orderDetails.id == id).first()

            if not del_order:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Order with the given ID doesn't exist"
                )
            order_status = db.query(orderDetails).filter(orderDetails.order_status)
            if  order_status == 'PENDING':
                raise HTTPException(
                   status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Sorry ,Your order has Done"
        ) 
            if not del_order:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Order with the given ID doesn't exist"
                )
            db.delete(del_order)
            db.commit()   
            return {"message":'Your order has deleted'}
        except Exception as err:
            return {'name':str(err),'Descritption':sys.exc_info()[1]}

