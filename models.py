import string
from database import Base
from sqlalchemy import Column,Integer,Boolean,Text,String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

from database import Base


class User(Base):
    __tablename__='customers'
    id=Column(Integer,primary_key=True)
    phone=Column(Integer,primary_key=True)
    name=Column(String(25),unique=True)
    location = Column(string)
    orders=relationship('Order',back_populates='customer')


class Order(Base):

    ORDER_STATUSES=(
        ('PENDING','pending'),
        ('IN-TRANSIT','in-transit'),
        ('DELIVERED','delivered')

    )

    PIZZA_SIZES=(
        ('SMALL','small'),
        ('MEDIUM','medium'),
        ('LARGE','large'),
        ('EXTRA-LARGE','extra-large')
    )


    __tablename__='orders'
    id=Column(Integer,primary_key=True)
    order_status=Column(ChoiceType(choices=ORDER_STATUSES),default="PENDING")
    order_size=Column(ChoiceType(choices=PIZZA_SIZES),default="SMALL")
    order_id=Column(Integer,ForeignKey('user.id'))
    owner=relationship('User',back_populates='orders')

    