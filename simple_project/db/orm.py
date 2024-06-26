import random
# from psycopg.errors import InvalidTextRepresentation
# from sqlalchemy.ext import
from sqlalchemy import select
from .database import Base
from .database import sync_engine, sync_session
from .models import Numbers


def insert_data(value):
    try:
        with sync_session() as session:
            some_value = Numbers(value=value)
            session.add(some_value)
            session.commit()
    except Exception:
        return None


def create_tables():
    Base.metadata.drop_all(bind=sync_engine)
    Base.metadata.create_all(bind=sync_engine)
    insert_data(43)
    insert_data(52)
    insert_data(24)
    insert_data(67)


def get_number():
    with sync_session() as session:
        stmt_1 = select(Numbers.id)
        req = session.execute(stmt_1)
        res = req.scalars().all()[-1]
        random_number = random.randint(1, res)

        stmt_2 = select(Numbers).where(Numbers.id == random_number)
        a = session.execute(stmt_2)
        number = a.scalar().value

    return number
