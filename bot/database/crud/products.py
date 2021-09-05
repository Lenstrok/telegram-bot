from typing import Optional

from sqlalchemy import select

from bot.database.models import Product
from bot.database.engine import Session


def get(session: Session, id: int) -> Optional[Product]:
    """Получить продукт из базы данных."""
    return session.execute(
        select(Product).
            filter_by(id=id)
    ).scalars().first()


def get_by_name(session: Session, product_name: str) -> Optional[Product]:
    """Получить продукт из базы данных по названию."""
    return session.execute(
        select(Product).
        filter_by(name=product_name)
    ).scalars().first()
