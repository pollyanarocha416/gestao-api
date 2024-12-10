from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from config import Banco
from datetime import date
from enum import Enum as PyEnum


class Products(Banco):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    valor = Column(Integer)
    quantidade = Column(Integer)
