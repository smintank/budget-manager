from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

DATABASE_URL = 'postgresql+asyncpg://user:password@localhost/db'

engine = create_async_engine(DATABASE_URL, echo=True)
Session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def get_db():
    async with Session() as session:
        yield session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_async(Base.metadata.create_all)
