from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schema.schemas import Product, SimpleProduct, ProductDefalt
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repository.products import RepositoryProduct

router: APIRouter = APIRouter()

@router.post("/products", status_code=status.HTTP_201_CREATED, response_model=SimpleProduct)
def create_product(product: Product, db: Session = Depends(get_db)):
    prouct_created = RepositoryProduct(db).create(product)
    return prouct_created

@router.get("/products", status_code=status.HTTP_200_OK, response_model=List[SimpleProduct])
def products_list(db: Session = Depends(get_db)):
    query_products = RepositoryProduct(db).all()
    return query_products

@router.get("/products/{id}", response_model=SimpleProduct)
def get_product(id: int, db: Session = Depends(get_db)):
    product = RepositoryProduct(db).get(id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'product with id "{id}" not found')
    return product

@router.get("/products/{user_id}/my_products", response_model=List[ProductDefalt])
def get_product(user_id: int, db: Session = Depends(get_db)):
    product = RepositoryProduct(db).my_products(user_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id "{id}" not found')
    return product

@router.put("/products/{id}", response_model=SimpleProduct)
def product_update(id: int, product: Product,db: Session = Depends(get_db)):
    RepositoryProduct(db).update(id, product)
    product.id = id
    return product

@router.delete("/products/{id}")
def product_remove(id: int,db: Session = Depends(get_db)):
    RepositoryProduct(db).delete(id)
    return {"message": "Product, deleted successfully"}