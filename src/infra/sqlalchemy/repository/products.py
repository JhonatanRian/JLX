from typing import List
from sqlalchemy import update, delete
from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models

class RepositoryProduct():
	def __init__(self: object, session: Session) -> None:
		"""constructor of class

		Args:
			self (object): instantiated object
			session (Session): connection to database
		"""
		self.session: Session = session

	def create(self: object, product: schemas.Product) -> models.Product:
		"""Create new product

		Args:
			self (object): instantiated object
			product (schemas.Product): scheme of a requested product

		Returns:
			models.Product: Model of a product in the database
		"""
		product_model = models.Product(
			name=product.name,
			details=product.details,
			price=product.price,
			disponible=product.disponible,
			user_id=product.user_id
			)
		self.session.add(product_model)
		self.session.commit()
		self.session.refresh(product_model)
		return product_model


	def all(self: object) -> List[models.Product]:
		"""Capture all products in database

		Args:
			self (object): instantiated object

		Returns:
			List[models.Product]: list of products
		"""
		query_products: List[models.Product] = self.session.query(models.Product).all()
		return query_products

	def update(self: object, product: schemas.Product) -> models.Product:
		stmt = update(models.Product).where(models.Product.id == product.id).values(
			name=product.name,
			details=product.details,
			price=product.price,
			disponible=product.disponible,
			user_id=product.user_id
		)
		self.session.execute(stmt)
		self.session.commit()

	def get(self: object):
		...

	def delete(self: object, id: int):
		stmt = delete(models.Product).where(models.Product.id == id)
		self.session.execute(stmt)
		self.session.commit()