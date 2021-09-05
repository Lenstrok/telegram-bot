from typing import Optional

from sqlalchemy import update, delete

from bot.database.models import User
from bot.database.engine import Session


def create_user(id: int) -> None:
    """Создать пользователя в базе данных."""
    with Session() as session:
        session.add(User(id=id))
        session.commit()


def update_user(id: int, full_name: Optional[str] = None, phone_number: Optional[str] = None) -> None:
    """Обновить пользователя в базе данных."""
    with Session() as session:
        session.execute(
            update(User).
            where(User.id == id).
            values(full_name=full_name, phone_number=phone_number)
        )
        session.commit()


def delete_user(id: int) -> None:
    """Удалить пользователя из базы данных."""
    with Session() as session:
        session.execute(
            delete(User).
            where(User.id == id)
        )
        session.commit()
