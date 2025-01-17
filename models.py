from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from config import Banco


class Products(Banco):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    valor = Column(Integer)
    quantidade = Column(Integer)


class Usuario(Banco):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    senha = Column(String)
