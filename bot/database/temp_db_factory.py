from bot.database.db import DB
from bot.database.models import Base


if __name__ == '__main__':
    Base.metadata.create_all(DB)
