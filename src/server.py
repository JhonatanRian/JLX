from typing import List
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from src.schema.schemas import Product, SimpleProduct, SimpleUser, User
from src.infra.sqlalchemy.config.database import get_db, migrate
from src.infra.sqlalchemy.repository.products import RepositoryProduct
from src.infra.sqlalchemy.repository.user import RepositoryUser

migrate()

app = FastAPI()


### Products

@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=SimpleProduct)
def create_product(product: Product, db: Session = Depends(get_db)):
    prouct_created = RepositoryProduct(db).create(product)
    return prouct_created


@app.get("/products", status_code=status.HTTP_200_OK, response_model=List[SimpleProduct])
def products_list(db: Session = Depends(get_db)):
    query_products = RepositoryProduct(db).all()
    return query_products

@app.put("/products")
def product_update(product: Product,db: Session = Depends(get_db)):
    query_products = RepositoryProduct(db).update(product)
    return {"message": "Product, updated successfully"}

@app.delete("/products/{id}")
def product_remove(id: int,db: Session = Depends(get_db)):
    RepositoryProduct(db).delete(id)
    return {"message": "Product, deleted successfully"}

### Users

@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: User, session: Session = Depends(get_db)):
    user = RepositoryUser(session).create(user)
    return user

@app.get("/users", response_model=List[SimpleUser])
def user_list(db: Session = Depends(get_db)):
    query_users = RepositoryUser(db).all()
    return query_users