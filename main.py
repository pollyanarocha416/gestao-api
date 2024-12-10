from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, db
from config import engine
# from datetime import date


models.Banco.metadata.create_all(bind=engine)
app = FastAPI()


"""
    CRUD
"""
@app.get("/products/")
def get_products(db: Session = Depends(db.conection)):
    return db.query(models.Products).all()


@app.post("/products/")
def create_item(nome: str, descricao: str, valor:float, quantidade:int,
                 db: Session = Depends(db.conection)):

    db_products = models.Products(nome=nome, descricao=descricao, valor=valor, quantidade=quantidade)
    db.add(db_products)
    db.commit()
    db.refresh(db_products)
    return db_products


@app.put("/products/{item_id}")
def update_product(
    item_id: int, nome:str, descricao: str, valor:float, quantidade:int, db: Session = Depends(db.conection)
):
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
def delete_item(item_id: int, db: Session = Depends(db.conection)):
    db_product = db.query(models.Products).filter(models.Products.id == item_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_product)
    db.commit()
    return {"detail": "Item deleted"}


"""
    More roters
"""
