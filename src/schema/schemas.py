from pydantic import BaseModel
from typing import List, Optional


class Product(BaseModel):
	id: Optional[str] = None
	# user: Usuario
	name: str
	details: str
	price: float
	disponible: bool

	class Config:
		orm_mode = True

class SimpleProduct(BaseModel):
	id: Optional[str] = None
	# user: Usuario
	name: str
	price: float

	class Config:
		orm_mode = True

class User(BaseModel):
	id: Optional[str] = None
	name: str
	fone: str

class Request(BaseModel):
	id: Optional[str] = None
	user: User
	quantity: int
	delivery: bool = False
	address: str
	observation: Optional[str] = "Not observation"
