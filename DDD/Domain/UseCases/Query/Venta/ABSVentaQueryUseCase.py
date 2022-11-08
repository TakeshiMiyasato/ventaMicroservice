import uuid
from abc import ABC, abstractmethod
from typing import Optional, List

from DDD.Domain.UseCases.Query.Venta.ABSVentaQueryService import VentaQueryService
from DDD.Infraestructure.ReadModels.venta_read_model import VentaReadModel


class VentaQueryUseCase(ABC):
    @abstractmethod
    def fetch_venta_by_id(self, id: uuid.UUID) -> Optional[VentaReadModel]:
        raise NotImplementedError

    @abstractmethod
    def fetch_ventas_by_clienteId(self, clienteId: uuid.UUID) -> List[VentaReadModel]:
        raise NotImplementedError


class VentaQueryUseCaseImpl(VentaQueryUseCase):
    def __init__(self, venta_query_service: VentaQueryService):
        self.ventas_query_service: VentaQueryService = venta_query_service

    def fetch_venta_by_id(self, id: uuid) -> Optional[VentaReadModel]:
        try:
            venta = self.ventas_query_service.find_by_venta_id(id)
        except:
            raise
        return venta

    def fetch_ventas_by_clienteId(self, clienteId: uuid) -> List[VentaReadModel]:
        try:
            ventas = self.ventas_query_service.find_all_by_clienteId(clienteId)
        except:
            raise

        return ventas
