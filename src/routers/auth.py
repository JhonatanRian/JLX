from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.routers.auth_utils import get_logger_user
from src.schema.schemas import SimpleUser, User, Login, LoginSuccess
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repository.user import RepositoryUser
from src.infra.providers import hash_provider, token_provider

router: APIRouter = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=SimpleUser)
def signup(user: User, session: Session = Depends(get_db)):
    ### Check existence
    demand_user = RepositoryUser(session).get_for_email(user.email)
    if demand_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already exists")

    user.password = hash_provider.hash_generate(user.password)
    user = RepositoryUser(session).create(user)
    return user

@router.post("/token")
def login(login_scheme: Login, session: Session = Depends(get_db)) -> models.User:
    password = login_scheme.password
    email = login_scheme.email

    user = RepositoryUser(session).get_for_email(email)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect phone or password")

    password_validate = hash_provider.hash_verify(password, user.password)
    if not password_validate:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect phone or password")

    token = token_provider.create_access_token({"sub": user.email})

    return LoginSuccess(user=user, access_token=token)

@router.get("/Me", response_model=SimpleUser)
def me(user: User = Depends(get_logger_user), session: Session = Depends(get_db)):
    return user