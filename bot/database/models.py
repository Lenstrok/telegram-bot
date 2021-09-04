from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(255))
    phone_number = Column(String(25))

    basket = relationship("Basket")


class Basket(Base):
    __tablename__ = 'basket'

    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    delivery_id = Column(Integer)
    address_to = Column(String(1000))

    basket = relationship("Product")

    user_id = Column(Integer, ForeignKey('user.id'))


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    price = Column(Integer)

    basket_id = Column(Integer, ForeignKey('basket.id'))
