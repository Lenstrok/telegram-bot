from typing import Optional

from sqlalchemy import update as update_, delete as delete_

from bot.database.models import User
from bot.database.engine import Session
from bot.database.crud import orders


def create(session: Session, id: int) -> int:
    """Создать пользователя в базе данных."""
    session.add(User(id=id))
    orders.create(session, user_id=id)
    return id


def get_by_id(session: Session, id: int) -> User:
    """Получить пользователя из базы данных по id."""
    return session.get(User, id)


def update(session: Session, id: int, full_name: Optional[str] = None, phone_number: Optional[str] = None) -> None:
    """Обновить пользователя в базе данных."""
    session.execute(
        update_(User).
        where(User.id == id).
        values(full_name=full_name, phone_number=phone_number)
    )


def delete_by_id(session: Session, id: int) -> None:
    """Удалить пользователя из базы данных."""
    orders.delete_by_user_id(session=session, user_id=id)
    session.execute(
        delete_(User).
        where(User.id == id)
    )
