from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URL, SessionLocal


# Função para obter a sessão do banco de dados
def conection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
