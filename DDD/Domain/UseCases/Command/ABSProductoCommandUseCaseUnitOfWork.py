import uuid
from abc import ABC, abstractmethod
from typing import Optional, cast

from DDD.Domain.Model.Producto.producto import Producto
from DDD.Domain.Respositories.ABSproducto_repository import ProductoRepository
from DDD.Infraestructure.ReadModels.producto_read_model import ProductoReadModel
from DDD.Infraestructure.WriteModels.ProductoWriteModel import ProductoWriteModel


class ProductoCommandUseCaseUnitOfWork(ABC):
    producto_repository: ProductoRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class ProductoCommandUseCase(ABC):
    @abstractmethod
    def create_producto(self, data: ProductoWriteModel) -> Optional[ProductoReadModel]:
        raise NotImplementedError

    @abstractmethod
    def update_producto(self, id: uuid.UUID, data: ProductoWriteModel) -> Optional[ProductoReadModel]:
        raise NotImplementedError

    @abstractmethod
    def delete_producto_by_id(self, id: uuid.UUID):
        raise NotImplementedError


class ProductoCommandUseCaseImpl(ProductoCommandUseCase):
    def __init__(self, uow: ProductoCommandUseCaseUnitOfWork):
        self.uow: ProductoCommandUseCaseUnitOfWork = uow

    def create_producto(self, data: ProductoWriteModel) -> Optional[ProductoReadModel]:
        try:
            id = uuid.uuid4()
            nombre = data.nombre
            descripcion = data.descripcion
            precio = data.precio
            stock = data.stock
            producto = Producto(id, nombre, descripcion, precio, stock)

            self.uow.producto_repository.create(producto)
            self.uow.commit()

            created_producto = self.uow.producto_repository.find_by_id(id)
        except:
            self.uow.rollback()
            raise

        return ProductoReadModel.from_entity(cast(Producto, created_producto))

    def update_producto(self, id: uuid.UUID, data: ProductoWriteModel) -> Optional[ProductoReadModel]:
        try:
            existing_producto = self.uow.producto_repository.find_by_id(id)
            if existing_producto is None:
                raise 'El producto no ha sido encontrado'

            producto = Producto(
                id = id,
                nombre = data.nombre,
                descripcion= data.descripcion,
                precio= data.precio,
                stock= data.stock
            )

            self.uow.producto_repository.update(producto)

            updated_producto = self.uow.producto_repository.find_by_id(id)
            self.uow.commit()
        except:
            self.uow.rollback()
            raise

        return ProductoReadModel.from_entity(cast(Producto, updated_producto))

    def delete_producto_by_id(self, id: uuid.UUID):
        try:
            existing_producto = self.uow.producto_repository.find_by_id(id)
            if existing_producto is None:
                raise 'El producto no ha sido encontrado'
            self.uow.producto_repository.delete_by_id(id)
            self.uow.commit()
        except:
            self.uow.rollback()
            raise
