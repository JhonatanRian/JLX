from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from src.schema.schemas import InputRequest, OutputRequest
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repository.requests import RepositoryRequests

router: APIRouter = APIRouter()

@router.post("/requests", status_code=status.HTTP_201_CREATED, response_model=OutputRequest)
def create_request(request: InputRequest, db: Session = Depends(get_db)):
    request_created = RepositoryRequests(db).create(request)
    return request_created

@router.get("/requests/{id}", response_model=OutputRequest)
def view_request(id: int, db: Session = Depends(get_db)):
    try:
        request_ = RepositoryRequests(db).get_id(id)
        return request_
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'request with id "{id}" not found')

@router.get("/requests/{user_id}/purchased", response_model=List[OutputRequest])
def requests_purchased(user_id: int, db: Session = Depends(get_db)):
    purchased = RepositoryRequests(db).purchased(user_id)
    return purchased

@router.get("/requests/{user_id}/sold", response_model=List[OutputRequest])
def requests_sold(user_id: int, db: Session = Depends(get_db)):
    purchased = RepositoryRequests(db).sold(user_id)
    return purchased