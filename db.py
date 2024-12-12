from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URL, SessionLocal


def conection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
