import uuid
from abc import ABC, abstractmethod
from typing import Optional, List

from DDD.Infraestructure.ReadModels.producto_read_model import ProductoReadModel
from DDD.Domain.UseCases.Query.Producto.ABSProductoQueryService import ProductoQueryService


class ProductoQueryUseCase(ABC):
    @abstractmethod
    def fetch_producto_by_id(self, id: uuid.UUID) -> Optional[ProductoReadModel]:
        raise NotImplementedError

    @abstractmethod
    def fetch_all_productos(self) -> List[ProductoReadModel]:
        raise NotImplementedError


class ProductoQueryUseCaseImpl(ProductoQueryUseCase):
    def __init__(self, producto_query_service: ProductoQueryService):
        self.producto_query_service: ProductoQueryService = producto_query_service

    def fetch_producto_by_id(self, id: uuid.UUID) -> Optional[ProductoReadModel]:
        try:
            producto = self.producto_query_service.find_by_id(id)
        except:
            raise
        return producto

    def fetch_all_productos(self) -> List[ProductoReadModel]:
        try:
            productos = self.producto_query_service.find_all()
        except:
            raise
        return productos