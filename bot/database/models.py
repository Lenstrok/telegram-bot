from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(255))
    phone_number = Column(String(25))

    order = relationship("Order")


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Integer)
    delivery_id = Column(Integer)
    address_to = Column(String(1000))

    ordered_product = relationship("OrderedProduct")

    user_id = Column(Integer, ForeignKey('user.id'), unique=True)


class OrderedProduct(Base):
    __tablename__ = 'ordered_product'

    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    count = Column(Integer)


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    price = Column(Integer)

    ordered_product = relationship("OrderedProduct")
