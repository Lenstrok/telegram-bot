from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, doc="Идентификатор")
    full_name = Column(String(255), doc="ФИО")
    phone_number = Column(String(25), doc="Номер телефона")

    order = relationship("Order")


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True, doc="Идентификатор")
    price = Column(Integer, doc="Итоговая цена")
    delivery_id = Column(Integer, doc="Способ доставки")
    address_to = Column(String(1000), doc="Адрес доставки")
    user_id = Column(Integer, ForeignKey('user.id'), unique=True, doc="Идентификатор пользователя")

    ordered_product = relationship("OrderedProduct")



class OrderedProduct(Base):
    __tablename__ = 'ordered_product'

    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True, doc="Идентификатор заказа")
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True, doc="Идентификатор товара")
    count = Column(Integer, doc="Количество")


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, doc="Идентификатор")
    name = Column(String(255), unique=True, doc="Наименование")
    price = Column(Integer, doc="Цена")

    ordered_product = relationship("OrderedProduct")
