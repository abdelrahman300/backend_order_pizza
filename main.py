from gettext import find
from hashlib import new
from lib2to3.pgen2.token import NAME
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

Base.metadata.create_all(bind=engine)

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def response_order(id: int, quantity: int, pizza_size: str, order_status: str,order_location):
    
    response = {
        "quantity": quantity,
        "pizzuvicorn main:appa_size": pizza_size,
        "order_status": order_status,
        "order_location":order_location
    }
    return response


#create user
@app.post('/create/user',status_code=status.HTTP_201_CREATED)
def create_user(add_user:SignUpModel , db: Session = Depends(get_db)):
        try:   
                user_phone = db.query(user).filter(user.phone==add_user.phone).first()
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
                new_user.name = add_user.name,
                new_user.Phone = add_user.phone, 
                db.add(new_user)
                db.commit()
                
                return {'detail':'Your account created',
                'Your_id':new_user.id}#
        except Exception as err:
            return {'name':str(err),'Descritption':sys.exc_info()[1]}
#Create order

@app.post('/creat/order',status_code=status.HTTP_404_NOT_FOUND)
def create_order(user_:create_order_user,order:OrderModel,db:Session = Depends(get_db)):
    user_find= db.query(user).filter(user.phone==user_.phone).first()
    if not user_find:
        raise HTTPException(status_code=404, detail="You have to create account")
    new_order = orderDetails()
    new_order.name=order.name
    new_order.pizza_size = order.pizza_size,
    new_order.order_status=order.order_status,
    new_order.quantity = order.quantity
    new_order.location=order.location
    db.add(new_order)
    db.commit()
    #db.refresh(new_order)
    return jsonable_encoder(
        response_order(
         new_order.quantity, new_order.pizza_size, new_order.order_status,new_order.location
        ))

# #to get order by id

# @app.post('/creat/order',status_code=status.HTTP_404_NOT_FOUND)
# def create_order(user_:create_order_user,order:OrderModel,db:Session = Depends(get_db)):
#     user_find= db.query(user).filter(user.phone==user_.phone).first()
#     if not user_find:
#         raise HTTPException(status_code=404, detail="You have to create account")
#     new_order = OrderDetails()
#     new_order.name=order.name
#     new_order.pizza_size = order.pizza_size,
#     new_order.quantity = order.quantity
    
#     db.add(new_order)
#     db.commit()
#     #db.refresh(new_order)
#     return jsonable_encoder(
#         response_order(
#          new_order.quantity, new_order.pizza_size, new_order.order_status,new_order.location
#         ))

# #to get order by id
# @app.get('/get_order/{id}',status_code=status.HTTP_404_NOT_FOUND)
# def get_order(id:int,db:Session =Depends(get_db)):
#     find_user= db.query(user).filter(user.id==id)
#     if not find_user:
#         raise HTTPException(status_code=404, detail=f"You ID {id} not found ")
#     find_order = db.query(OrderDetails).filter(OrderDetails.id == id).filter(OrderDetails.id==user.get(id)).first()
#     if not find_order:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Order with the given ID{id} doesn't exist"
#         )
    
#     return jsonable_encoder(find_order)
# #get all orders
# @app.get('/all')
# def list_all_orders(db:Session = Depends(get_db)):

#     orders = db.query(OrderDetails).all()

#     if not orders:
#         return {"message":"No orders were made yet"}

#     orders =db.query(order).all()


#     return jsonable_encoder(orders)
# @app.put('/update_order/{id}')
# def update(id:int,db: Session = Depends(get_db)):
#     order_to_update=db.query(order).filter(order.id == id).first()
#     user_id=db.query(user).filter(id==user.get(id))
#     order_status = db.query(OrderDetails).filter(OrderDetails.order_status)
#     if not order_status in ['PENDING', 'IN-TRANSIT', 'DELIVERED']:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Wrong order status, available statuses are: PENDING, IN-TRANSIT, DELIVERED"
#     )    
        
#     if not order_to_update:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Order with the given ID doesn't exist"
#         )

#     order_to_update.quantity = OrderDetails.quantity
#     order_to_update.pizza_size =OrderDetails.pizza_size
#     db.commit()
#     #db.refresh(order_to_update.quantity, order_to_update.pizza_size)

#     return jsonable_encoder(
#         response_order(
#          order_to_update.quantity, order_to_update.pizza_size, order_to_update.order_status
#         ))  
        
# @app.delete('/delete/{id}')
# def Delete_order(id:int,db: Session = Depends(get_db)):
#     del_order= db.query(order).filter(order.id == id).first()
#     if not order:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Order with the given ID doesn't exist"
#         )
#     order_status = db.query(OrderDetails).filter(OrderDetails.order_status)
   
#     if not order_status in ['PENDING', 'IN-TRANSIT', 'DELIVERED']:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Wrong order status, available statuses are: PENDING, IN-TRANSIT, DELIVERED"
#     )    
#     if not del_order:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Order with the given ID doesn't exist"
#         )
#     db.delete(del_order)
#     db.commit()   
#     return 'Your order has deleted'