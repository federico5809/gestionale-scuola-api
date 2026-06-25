from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from contextlib import asynccontextmanager

from app.core.config import config

class Database:
    def __init__(self):
        self.engine = None
        self.SessionLocal = None

    async def start(self):
        """Initialize connection and start the pool"""
        if self.engine is not None:
            return

        host = config.DB_HOST
        port = config.DB_PORT
        db_name = config.DB_NAME
        user = config.DB_USER.get_secret_value()
        password = config.DB_PASSWORD.get_secret_value()

        url = f"postgresql+psycopg_async://{user}:{password}@{host}:{port}/{db_name}"
        
        try:
            self.engine = create_async_engine(
                url, 
                pool_size=5, 
                max_overflow=10,
                pool_pre_ping=True 
            )
            self.SessionLocal = async_sessionmaker(
                autocommit=False, 
                autoflush=False, 
                bind=self.engine,
                class_=AsyncSession
            )
        except Exception as e:
            raise e

    async def stop(self):
        """Stop all the connection to the pool"""
        if self.engine:
            await self.engine.dispose()
            self.engine = None

    @asynccontextmanager
    async def get_session(self):
        """Get a secure session that automatically close at the end"""
        if self.SessionLocal is None:
            self.start()
        
        session = self.SessionLocal()
        try:
            yield session
            await session.commit() 
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

db = Database()