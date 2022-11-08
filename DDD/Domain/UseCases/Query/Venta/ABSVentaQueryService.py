import uuid
from abc import ABC, abstractmethod
from typing import List

from DDD.Infraestructure.ReadModels.venta_read_model import VentaReadModel


class VentaQueryService(ABC):
    @abstractmethod
    def find_all_by_clienteId(self, clienteId: uuid) -> List[VentaReadModel]:
        raise NotImplementedError

    def find_by_venta_id(self, id: uuid) -> VentaReadModel:
        raise NotImplementedError