from bot.database.engine import engine
from bot.database.models import Base


if __name__ == '__main__':
    Base.metadata.create_all(engine)
