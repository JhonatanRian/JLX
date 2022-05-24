from pydantic import BaseModel
from typing import List, Optional
# uvicorn src.server:app --reload --reload-dir=src

class User(BaseModel):
	name: str
	# email: str
	password: str
	fone: str
	
	class Config:
		orm_mode = True

class Product(BaseModel):
	name: str
	details: str
	price: float
	disponible: bool
	user_id: int

	class Config:
		orm_mode = True

class ProductDefalt(BaseModel):
	id: int
	name: str
	disponible: bool
	price: float
	details: str

	class Config:
		orm_mode = True

class UserDefalt(BaseModel):
	id: int
	name: str
	fone: str
	products: List[ProductDefalt]

	class Config:
		orm_mode = True

class SimpleUser(BaseModel):
	id: Optional[int]  = None
	name: str
	fone: str

	class Config:
		orm_mode = True

class SimpleProduct(BaseModel):
	id: int
	name: str
	disponible: bool
	price: float
	details: str
	user: SimpleUser

	class Config:
		orm_mode = True


class InputRequest(BaseModel):
	locale_delivery: Optional[str]
	type_delivery: str
	observation: Optional[str] = "Not observation"

	user_id: int
	product_id: int

class OutputRequest(BaseModel):
	id: int
	locale_delivery: Optional[str]
	type_delivery: str
	observation: Optional[str] = "Not observation"

	user: SimpleUser
	product: SimpleProduct

	class Config:
		orm_mode = True