from typing import List
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models


class RepositoryUser:

    def __init__(self: object, session: Session) -> None:
        self.session: Session = session

    def create(self: object, user: schemas.User) -> models.User:
        user_model: models.User = models.User(
            name=user.name,
            email=user.email,
            password=user.password,
            fone=user.fone
        )
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)
        return user_model

    def all(self: object) -> List[models.User]:
        stmt = select(models.User)
        users_models: List[models.User] = self.session.execute(stmt).scalars().all()
        return users_models

    # def update(self: object) -> models.User:
    #     stmt = update(models)

    def get_for_email(self: object, email: str) -> None:
        stmt = select(models.User).where(models.User.email == email)
        return self.session.execute(stmt).scalars().first()

    def remove(self: object) -> None:
        ...