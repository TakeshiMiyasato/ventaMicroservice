import uuid
from abc import ABC, abstractmethod
from typing import Optional, cast

from DDD.Domain.Model.Venta.detalleVenta import DetalleVenta
from DDD.Domain.Respositories.ABSdetalleVenta_repository import DetalleVentaRepository
from DDD.Infraestructure.ReadModels.detalle_venta_read_model import DetalleVentaReadModel
from DDD.Infraestructure.WriteModels.DetalleVentaWriteModel import DetalleVentaWriteModel


class DetalleVentaCommandUseCaseUnitOfWork(ABC):
    detalleVenta_repository = DetalleVentaRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class DetalleVentaCommandUseCase(ABC):
    @abstractmethod
    def create_detalleVenta(self, data: DetalleVentaWriteModel) -> Optional[DetalleVentaReadModel]:
        raise NotImplementedError


class DetalleVentaCommandUseCaseImpl(DetalleVentaCommandUseCase):
    def __init__(self, uow: DetalleVentaCommandUseCaseUnitOfWork):
        self.uow: DetalleVentaCommandUseCaseUnitOfWork = uow

    def create_detalleVenta(self, data: DetalleVentaWriteModel) -> Optional[DetalleVentaReadModel]:
        try:
            productoId = data.productoId
            ventaId = data.ventaId,
            cantidad = data.cantidad,
            subtotal = data.subtotal

            detalleVenta = DetalleVenta(productoId, ventaId, cantidad, subtotal)

            self.uow.detalleVenta_repository.create(detalleVenta)
            self.uow.commit()

        except:
            self.uow.rollback()
            raise

        return DetalleVentaReadModel.from_entity(cast(DetalleVenta, detalleVenta))
