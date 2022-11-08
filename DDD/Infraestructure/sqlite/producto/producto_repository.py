import uuid
from typing import Optional

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from DDD.Domain.Model.Producto.producto import Producto
from DDD.Domain.Respositories.ABSproducto_repository import ProductoRepository
from DDD.Infraestructure.sqlite.producto.producto_dto import ProductoDTO
from DDD.Domain.UseCases import ProductoCommandUseCaseUnitOfWork


class ProductoRepositoryImpl(ProductoRepository):
    def __init__(self, session: Session):
        self.session: Session = session

    def create(self, producto: Producto):
        producto_dto = ProductoDTO.from_entity(producto)
        try:
            self.session.add(producto_dto)
        except:
            raise

    def find_by_id(self, id: uuid.UUID) -> Optional[Producto]:
        try:
            producto_dto = self.session.query(ProductoDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return producto_dto.to_entity()

    def update(self, producto: Producto):
        producto_dto = ProductoDTO.from_entity(producto)
        try:
            _producto = self.session.query(ProductoDTO).filter_by(id=producto_dto.id).one()
            _producto.nombre = producto_dto.nombre
            _producto.descripcion = producto_dto.descripcion
            _producto.precio = producto_dto.precio
            _producto.stock = producto_dto.stock
        except:
            raise

    def delete_by_id(self, id: uuid.UUID):
        try:
            self.session.query(ProductoDTO).filter_by(id=id).delete()
        except:
            raise


class ProductoCommandUseCaseUnitOfWorkImpl(ProductoCommandUseCaseUnitOfWork):
    def __init__(self, session: Session, producto_repository: ProductoRepository):
        self.session: Session = session
        self.producto_repository: ProductoRepository = producto_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
