from typing import List
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from src.schema.schemas import Product, SimpleProduct
from src.infra.sqlalchemy.config.database import get_db, migrate
from src.infra.sqlalchemy.repository.products import RepositoryProduct

migrate()

app = FastAPI()


@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=SimpleProduct)
def create_product(product: Product, db: Session = Depends(get_db)):
    prouct_created = RepositoryProduct(db).create(product)
    return prouct_created


@app.get("/products", status_code=status.HTTP_200_OK, response_model=List[SimpleProduct])
def products_list(db: Session = Depends(get_db)):
    products = RepositoryProduct(db).all()
    return products