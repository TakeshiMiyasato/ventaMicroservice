import uuid
from abc import ABC, abstractmethod
from typing import Optional

from DDD.Domain.Model.Venta.venta import Venta
from DDD.SharedKernel.Core.ABSRepository import IRepository


class VentaRepository(ABC):
    @abstractmethod
    def create(self, venta: Venta) -> Optional[Venta]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: uuid) -> Optional[Venta]:
        raise NotImplementedError