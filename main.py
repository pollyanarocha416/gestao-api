from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import models, db
from config import engine
from enum import Enum
from pydantic import BaseModel
from typing import Union
from models import Products
from fastapi.middleware.cors import CORSMiddleware


models.Banco.metadata.create_all(bind=engine)
app = FastAPI()

# middleware para permitir CORS
origins = [
    "http://127.0.0.1:5500",  # URL do frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite as origens listadas
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)


@app.get("/usuarios/")
def get_usuarios(db: Session = Depends(db.conection)):
    users = db.query(models.Usuario).all()
    return users


@app.post("/usuarios/")
def create_item(email: str, senha: str, db: Session = Depends(db.conection)):
    try:
        db_usuarios = models.Usuario(email=email, senha=senha)
        db.add(db_usuarios)
        db.commit()
        db.refresh(db_usuarios)

        return db_usuarios
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
        )


@app.get("/products/")
def get_products(db: Session = Depends(db.conection)):

    return db.query(models.Products).all()


class Item(BaseModel):
    nome: str
    descricao: Union[str, None] = None
    valor: float
    quantidade: Union[float, None] = None


def create_sqlalchemy_item(item: Item):
    return Products(
        nome=item.nome,
        descricao=item.descricao,
        valor=item.valor,
        quantidade=item.quantidade,
    )


@app.post("/products/")
async def create_products(item: Item, db: Session = Depends(db.conection)):
    sqlalchemy_item = create_sqlalchemy_item(item)
    db.add(sqlalchemy_item)
    db.commit()
    db.refresh(sqlalchemy_item)

    return sqlalchemy_item


@app.put("/products/{item_id}")
def update_product(
    item_id: int,
    nome: str,
    descricao: str,
    valor: float,
    quantidade: int,
    db: Session = Depends(db.conection),
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


# teste
# class ModelFuncionarios(str, Enum):
#     joao = "joao"
#     mateus = "mateus"
#     julia = "julia"


# @app.get("/models/{model_funcionarios}")
# async def get_model(model_funcionarios: ModelFuncionarios):
#     if model_funcionarios is ModelFuncionarios.joao:
#         return {"model_name": model_funcionarios, "message": "TI"}

#     if model_funcionarios.value == "joao":
#         return {"model_name": model_funcionarios, "message": "TI Senior"}

#     return {"model_funcionarios": model_funcionarios, "message": "Outra area"}


@app.get("/documents/")
async def read_items(
    rg: Union[str, None] = Query(
        default=None, max_length=11, pattern="^[0-9]{1}\.[0-9]{3}\.[0-9]{3}-[0-9]{1}$"
    )
):
    # , pattern="^fixedquery$"  -> caso queira adicionar uma expreção regular
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if rg:
        results.update({"RG": rg})
    return results


@app.get("/time/")
async def read_items(jogadoras: Union[list[str], None] = Query(default=None)):
    query_items = {"jogadoras": jogadoras}
    return query_items


# teste
@app.get("/selecao/")
async def read_items(
    jogadoras: list[str] = Query(default=["gabi", "carol", "ana cristina"])
):
    query_items = {"jogadoras": jogadoras}
    return query_items
