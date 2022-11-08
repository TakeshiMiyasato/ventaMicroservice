import uuid
from abc import ABC, abstractmethod
from typing import Optional, List

from DDD.Infraestructure.ReadModels.detalle_venta_read_model import DetalleVentaReadModel


class DetalleVentaQueryService(ABC):
    @abstractmethod
    def find_all_by_id(self, id: uuid.UUID) -> List[DetalleVentaReadModel]:
        raise NotImplementedError