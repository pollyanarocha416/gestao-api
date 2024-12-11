from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from config import Banco
from datetime import date
from enum import Enum as PyEnum
from pydantic import BaseModel, Field, validator
from security import get_password_hash
import ormar
import re
from pydantic import validator


class Usuario(ormar.Model):
    class Meta:
        tablename = "usuarios"

    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100, unique=True)
    hash_password: str = ormar.String(max_length=255)

    @validator("email")
    def valida_formatacao_sigla(cls, v):
        if not re.compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        ).match(v):
            raise ValueError("The user email format is invalid!")
        return v


class Products(Banco):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    valor = Column(Integer)
    quantidade = Column(Integer)
