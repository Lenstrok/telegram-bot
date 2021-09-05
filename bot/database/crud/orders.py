from typing import Optional

from sqlalchemy import select, delete as delete_, update as update_

from bot.database.models import Order
from bot.database.engine import Session
from bot.database.crud import ordered_products, products


def create(session: Session, user_id: int) -> None:
    """Создать заказ для пользователя."""
    session.add(Order(user_id=user_id, price=0))


def add(session: Session, user_id: int, product_name: str):
    """Добавить позицию в заказ."""
    order = get_by_user_id(session, user_id)
    product = products.get_by_name(session, product_name)  # todo если None, выводить ошибку (обрабатывать через if)
    ordered_products.add(session, order.id, product.id)

    order = get_by_user_id(session, user_id)  # todo если None, выводить ошибку (обрабатывать через if)
    order.price += product.price


def get_by_user_id(session: Session, user_id: int) -> Optional[Order]:
    """Получить все заказы из базы данных по заданному id пользователя."""
    return session.execute(
        select(Order).
        filter_by(user_id=user_id)
    ).scalars().first()


def delete_by_user_id(session: Session, user_id: int) -> None:
    """Удалить заказ для пользователя из базы данных."""
    order = get_by_user_id(session, user_id)

    if order is not None:
        ordered_products.delete_by_order_id(session=session, order_id=order.id)

        session.execute(
            delete_(Order).
            where(Order.user_id == user_id)
        )
