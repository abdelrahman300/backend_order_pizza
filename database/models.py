from ast import Index
from enum import unique
from operator import index
from unicodedata import name
from sqlalchemy import Column, ForeignKey, Integer, String,Identity, true
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.choice import ChoiceType
from database.database import Base


class user(Base):
    __tablename__ = 'users'

    id = Column( Integer, Identity(start=1, cycle=True), primary_key=True)
    name = Column(String, unique=True)
    phone = Column(String,unique=True)
    orderd_detail = relationship('orderDetails', back_populates='Owner')

    
#OREDR TABLE
class order(Base):
    __tablename__ = 'order'
    id =  Column( Integer, Identity(start=1, cycle=True), primary_key=True)






class orderDetails(Base):
    ORDER_STATUSES = (
        ('PENDING', 'Pending'),
        ('IN-TRANSIT', 'In-Transit'),
        ('DELIVERED', 'Delivered')
    )

    PIZZA_SIZES = (
        ('SMALL', 'Small'),
        ('MEDIUM', 'Medium'),
        ('LARGE', 'Large'),
        ('EXTRA-LARGE', 'Extra-Large')
    )

    __tablename__ = 'orders_detail'
   #error here
    name = Column(String,primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default="PENDING")
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES), default="SMALL")
    location =Column(String)
    Owner_id = Column(Integer, ForeignKey('users.id'))
    Owner = relationship('user', back_populates='orderd_detail')
