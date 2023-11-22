from sqlalchemy import create_engine, Column, Integer, DateTime, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from config import DATABASE_URL

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, unique=True)
    last_interaction = Column(DateTime, default=datetime.utcnow)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def check_user_in_database(user_id):
    async with engine.connect() as connection:
        result = await connection.execute(select(
            User).where(
                User.chat_id == user_id))
        return result.scalar() is not None

async def register_user(user_id):
    async with engine.connect() as connection:
        user = User(chat_id=user_id)
        connection.execute(User.__table__.insert().values(user))

async def update_last_interaction(user_id):
    async with engine.connect() as connection:
        connection.execute(
            User.__table__.update().where(
                User.chat_id == user_id).values(
                    last_interaction=datetime.utcnow())
        )
