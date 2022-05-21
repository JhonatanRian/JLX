from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base

class User(Base):

	__tablename__ = "user"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)
	email = Column(String, unique=True, index=True)
	password = Column(String)
	fone = Column(String)
	products = relationship("Product", back_populates="user")

class Product(Base):

	__tablename__ = "product"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)
	details  = Column(String)
	price = Column(Float)
	disponible = Column(Boolean)
	user_id = Column(Integer, ForeignKey("user.id", name="fk_user"))
	user = relationship("User", back_populates="products")