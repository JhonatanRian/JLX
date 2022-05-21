from pydantic import BaseModel
from typing import List, Optional
# uvicorn src.server:app --reload --reload-dir=src

class User(BaseModel):
	id: Optional[int] = None
	name: str
	# email: str
	password: str
	fone: str
	
	class Config:
		orm_mode = True

class SimpleUser(BaseModel):
	id: Optional[int]  = None
	name: str
	fone: str

	class Config:
		orm_mode = True

class Product(BaseModel):
	id: Optional[str] = None
	user_id: int
	name: str
	details: str
	price: float
	disponible: bool

	class Config:
		orm_mode = True

class SimpleProduct(BaseModel):
	id: Optional[str] = None
	name: str
	disponible: bool
	price: float
	details: str
	user: Optional[SimpleUser]

	class Config:
		orm_mode = True


# class Request(BaseModel):
# 	id: Optional[str] = None
# 	user: User
# 	quantity: int
# 	delivery: bool = False
# 	address: str
# 	observation: Optional[str] = "Not observation"
