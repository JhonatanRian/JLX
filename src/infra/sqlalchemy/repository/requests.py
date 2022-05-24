from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models

class RepositoryRequests():

    def __init__(self: object, session: Session) -> None:
        self.session: Session = session

    def create(self: object, request: schemas.InputRequest) -> models.Request:
        request_model = models.Request(
            locale_delivery=request.locale_delivery,
            type_delivery=request.type_delivery,
            observation=request.observation if request.observation else ...,
            user_id=request.user_id,
            product_id=request.product_id
        )
        self.session.add(request_model)
        self.session.commit()
        self.session.refresh(request_model)
        return request_model

    def get_id(self: object, id: int) -> models.Request:
        consultation = select(models.Request).where(models.Request.id == id)
        request = self.session.execute(consultation).scalars().first()
        return request
    
    def purchased(self: object, user_id: int) -> List[models.Request]:
        consultation = select(models.Request).where(models.Request.user_id == user_id)
        requests = self.session.execute(consultation).scalars().all()
        return requests
    
    def sold(self: object, user_id: int) -> List[models.Request]:
        consultation = select(models.Request).join_from(models.Request, models.Product).where(models.Product.user_id == user_id)
        requests = self.session.execute(consultation).scalars().all()
        return requests