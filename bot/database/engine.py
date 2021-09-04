import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    f"sqlite:///{os.path.join(os.path.abspath(__file__).replace('engine.py', ''), 'example.db')}",
    echo=True,
    future=True
)

Session = sessionmaker(engine)
