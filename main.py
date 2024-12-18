from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, db
from config import engine
from enum import Enum
from pydantic import BaseModel
from typing import Union
from models import Products

models.Banco.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/products/")
def get_products(
            db: Session = Depends(db.conection)):

    return db.query(models.Products).all()


class Item(BaseModel):
    nome: str
    descricao: Union[str, None] = None
    valor: float
    quantidade: Union[float, None] = None


def create_sqlalchemy_item(item: Item):
    return Products(nome=item.nome, descricao=item.descricao, valor=item.valor, quantidade=item.quantidade)


@app.post("/products/")
async def create_products(item: Item, db: Session = Depends(db.conection)):
    sqlalchemy_item = create_sqlalchemy_item(item)
    db.add(sqlalchemy_item)
    db.commit()
    db.refresh(sqlalchemy_item)

    return sqlalchemy_item

# @app.post("/products/")
# def create_item(nome: str, descricao: str, valor:float, quantidade:int,
#                 db: Session = Depends(db.conection)):

#     db_products = models.Products(nome=nome, descricao=descricao, valor=valor, quantidade=quantidade)

#     db.add(db_products)
#     db.commit()
#     db.refresh(db_products)

#     return db_products


@app.put("/products/{item_id}")
def update_product(item_id: int, nome:str, descricao: str, valor:float, quantidade:int, 
                db: Session = Depends(db.conection)):

    db_product = db.query(models.Products).filter(models.Products.id == item_id).first()

    if db_product is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db_product.nome = nome
    db_product.descricao = descricao
    db_product.valor = valor
    db_product.quantidade = quantidade
    db.commit()
    db.refresh(db_product)

    return db_product


@app.delete("/products/{item_id}")
def delete_item(item_id: int, 
            db: Session = Depends(db.conection)):

    db_product = db.query(models.Products).filter(models.Products.id == item_id).first()

    if db_product is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_product)
    db.commit()

    return {"detail": "Item deleted"}


# teste


class ModelFuncionarios(str, Enum):
    joao = "joao"
    mateus = "mateus"
    julia = "julia"


@app.get("/models/{model_funcionarios}")
async def get_model(model_funcionarios: ModelFuncionarios):
    if model_funcionarios is ModelFuncionarios.joao:
        return {"model_name": model_funcionarios, "message": "TI"}

    if model_funcionarios.value == "joao":
        return {"model_name": model_funcionarios, "message": "TI Senior"}

    return {"model_funcionarios": model_funcionarios, "message": "Outra area"}
