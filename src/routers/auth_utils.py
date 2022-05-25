from fastapi import Depends, HTTPException,status
from jose import JWTError
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repository.user import RepositoryUser
from src.infra.providers import token_provider
from fastapi.security import OAuth2PasswordBearer
from src.infra.sqlalchemy.config.database import get_db

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

def get_logger_user(token: str = Depends(oauth2_schema), session: Session = Depends(get_db)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token")
    
    try:
        email = token_provider.verify_access_token(token)
    except JWTError:
        raise exception

    if not email:
        raise exception

    user = RepositoryUser(session).get_for_email(email)

    if not user:
        raise exception

    return user
