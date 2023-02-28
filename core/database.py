import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime, JSON, Text, select, insert, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

from core.config import settings

engine = create_async_engine(settings.DATABASE_URL)
Base = declarative_base()


async def init_models(s):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as s:
        yield s
