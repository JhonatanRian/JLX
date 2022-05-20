from typing import List
from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models

class RepositoryProduct():
	def __init__(self: object, db: Session) -> None:
		"""constructor of class

		Args:
			self (object): instantiated object
			db (Session): connection to database
		"""
		self.db: Session = db

	def create(self: object, product: schemas.Product):
		"""Create new product

		Args:
			self (object): instantiated object
			product (schemas.Product): scheme of a requested product

		Returns:
			models.Product: Model of a product in the database
		"""
		db_product = models.Product(
			name=product.name,
			details=product.details,
			price=product.price,
			disponible=product.disponible,
			)
		self.db.add(db_product)
		self.db.commit()
		self.db.refresh(db_product)
		return db_product


	def all(self: object):
		"""Capture all products in database

		Args:
			self (object): instantiated object

		Returns:
			List[models.Product]: list of products
		"""
		products: List[models.Product] = self.db.query(models.Product).all()
		return products

	def get(self: object):
		...

	def delete(self: object):
		...