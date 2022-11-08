import uuid
from abc import ABC, abstractmethod
from typing import List

from DDD.Infraestructure.ReadModels.detalle_venta_read_model import DetalleVentaReadModel
from DDD.Domain.UseCases.Query.Venta.ABSDetalleVentaQueryService import DetalleVentaQueryService


class DetalleVentaQueryUseCase(ABC):
    @abstractmethod
    def fetch_all_detalleVenta_by_ventaId(self, id: uuid.UUID) -> List[DetalleVentaReadModel]:
        raise NotImplementedError


class DetalleVentaQueryUseCaseImpl(DetalleVentaQueryUseCase):
    def __init__(self, detalleVenta_query_service: DetalleVentaQueryService):
        self.detalleVenta_query_service: DetalleVentaQueryService = detalleVenta_query_service

    def fetch_all_detalleVenta_by_ventaId(self, id: uuid.UUID) -> List[DetalleVentaReadModel]:
        try:
            detallesVenta = self.detalleVenta_query_service.find_all_by_id(id)
        except:
            raise
        return detallesVenta

