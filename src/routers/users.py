from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.schema.schemas import SimpleUser, UserDefalt, User
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repository.user import RepositoryUser

router: APIRouter = APIRouter()

@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=SimpleUser)
def create_user(user: User, session: Session = Depends(get_db)):
    user = RepositoryUser(session).create(user)
    return user

@router.get("/users", response_model=List[UserDefalt])
def user_list(db: Session = Depends(get_db)):
    query_users = RepositoryUser(db).all()
    return query_users