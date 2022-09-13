from ast import Index
from enum import unique
from operator import index
import string
from unicodedata import name
from sqlalchemy import Column, ForeignKey, Integer, String,Identity, true
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.choice import ChoiceType
from database.database import Base
#, Identity(start=1, cycle=True),primary_key=True

class user(Base):
    __tablename__ = 'users'
    id = Column(  Integer, Identity(start=1, cycle=True), primary_key=True)
    name = Column(String, unique=True)
    phone = Column(String,unique=True)
    orders_detail = relationship('orderDetails', back_populates='Owner')

    
#OREDR TABLE
# class order(Base):
#     __tablename__ = 'order'
#     id =  Column( Integer, Identity(start=1, cycle=True), primary_key=True)


class orderDetails(Base):
    ORDER_STATUSES = (
        ('PENDING', 'pending'),
        ('IN-TRANSIT', 'in-Transit'),
        ('DELIVERED', 'delivered')
    )
    __tablename__ = 'orders_detail'
    #error here
    id=Column(  Integer, Identity(start=1, cycle=True), primary_key=True)
    name = Column(String,unique=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default="PENDING")
    pizza_size = Column(String, default="SMALL")
    location =Column(String)
    Owner_id = Column(Integer, ForeignKey('users.id'))
    Owner = relationship('user', back_populates='orders_detail')
