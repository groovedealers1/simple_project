from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from .config import settings


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True)

async_session = async_sessionmaker(bind=async_engine)
sync_session = sessionmaker(bind=sync_engine)


class Base(DeclarativeBase): pass
