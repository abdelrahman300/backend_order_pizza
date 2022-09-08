from enum import unique
from unicodedata import name
from sqlalchemy import Column, ForeignKey, Integer, String,Identity
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.choice import ChoiceType
from database import Base


class User(Base):
    __tablename__ = 'User'

    id = Column( Integer, Identity(start=1, cycle=True), primary_key=True)
    name = Column(String, unique=True)
    phone = Column(String,unique=True)

   # orders = relationship('OrderDetils','Order', back_populates='user')

    

class Order(Base):
    __tablename__ = 'Order'
    id = Column( Integer, Identity(start=1, cycle=True), primary_key=True)
class OrderDetails(Base):
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

    __tablename__ = 'Orders'

    name = Column(String, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default="PENDING")
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES), default="SMALL")
    user_id = Column(Integer, ForeignKey('User.id'))
   # user = relationship('User', back_populates='OrderDetails')
