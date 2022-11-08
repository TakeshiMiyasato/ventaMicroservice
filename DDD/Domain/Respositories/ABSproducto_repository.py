import uuid
from abc import ABC, abstractmethod
from typing import Optional

from DDD.Domain.Model.Producto.producto import Producto
from DDD.SharedKernel.Core.ABSRepository import IRepository


class ProductoRepository(ABC):
    @abstractmethod
    def create(self, producto: Producto):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_id(self, id: uuid.UUID) -> Optional[Producto]:
        raise NotImplementedError

    @abstractmethod
    def update(self, producto: Producto):
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: uuid.UUID):
        raise NotImplementedError