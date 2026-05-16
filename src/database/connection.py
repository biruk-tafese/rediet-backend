# src/database/connection.py
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from src.config import settings

# 1. Create the Async Engine
# pool_pre_ping=True is essential for serverless DBs like Neon to handle cold starts/dropped connections safely
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False, # Set to True if you want to see raw SQL logs in development
    pool_pre_ping=True
)

# 2. Create the Session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)

# 3. Base class for our Models to inherit from
class Base(DeclarativeBase):
    pass

# 4. Dependency injection helper for FastAPI routes
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()