import uuid
from abc import ABC, abstractmethod
from typing import Optional, List

from DDD.Infraestructure.ReadModels.producto_read_model import ProductoReadModel


class ProductoQueryService(ABC):
    @abstractmethod
    def find_by_id(self, id: uuid.UUID) -> Optional[ProductoReadModel]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[ProductoReadModel]:
        raise NotImplementedError
