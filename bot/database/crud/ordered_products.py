from typing import Optional

from sqlalchemy import delete as delete_, select

from bot.database.models import OrderedProduct
from bot.database.engine import Session


def add(session: Session, order_id: int, product_id: int) -> None:
    """Добавить заказанный товар."""
    ordered_product = get(session, order_id, product_id)

    if ordered_product is None:
        session.add(OrderedProduct(order_id=order_id, product_id=product_id, count=1))
    else:
        ordered_product.count += 1


def get(session: Session, order_id: int, product_id: int) -> Optional[OrderedProduct]:
    """Получить заказанный товар."""
    return session.execute(
        select(OrderedProduct).
        filter_by(order_id=order_id, product_id=product_id)
    ).scalars().first()


def delete_by_order_id(session: Session, order_id: int) -> None:
    """Удалить ВСЕ заказаннае товары из базы данных по id заказа."""
    session.execute(
        delete_(OrderedProduct).
        where(OrderedProduct.order_id == order_id)
    )
