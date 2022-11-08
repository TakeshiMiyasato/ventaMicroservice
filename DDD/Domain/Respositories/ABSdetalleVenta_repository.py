import uuid
from abc import ABC, abstractmethod
from typing import List, Optional

from DDD.Domain.Model.Venta.detalleVenta import DetalleVenta
from DDD.SharedKernel.Core.ABSRepository import IRepository


class DetalleVentaRepository(ABC):
    @abstractmethod
    def create(self, detalleVenta: DetalleVenta):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: uuid) -> Optional[DetalleVenta]:
        raise NotImplementedError