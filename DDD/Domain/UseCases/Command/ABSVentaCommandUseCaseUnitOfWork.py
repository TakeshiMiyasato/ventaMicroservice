import uuid
from abc import ABC, abstractmethod
from typing import Optional, cast

from DDD.Domain.Model.Venta.venta import Venta
from DDD.Domain.Respositories.ABSventa_repository import VentaRepository
from DDD.Infraestructure.ReadModels.venta_read_model import VentaReadModel
from DDD.Infraestructure.WriteModels.VentaWriteModel import VentaWriteModel
from DDD.SharedKernel.ValueObjects.TotalValid import Total


class VentaCommandUseCaseUnitOfWork(ABC):
    venta_repository: VentaRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class VentaCommandUseCase(ABC):
    @abstractmethod
    def create_venta(self, data: VentaWriteModel) -> Optional[VentaReadModel]:
        raise NotImplementedError


class VentaCommandUseCaseImpl(VentaCommandUseCase):
    def __init__(self, uow: VentaCommandUseCaseUnitOfWork):
        self.uow: VentaCommandUseCaseUnitOfWork = uow

    def create_venta(self, data: VentaWriteModel) -> Optional[VentaReadModel]:
        try:
            id = uuid.uuid4()
            total = Total(data.total)
            clienteId = data.clienteId
            venta = Venta(id, total, clienteId)

            self.uow.venta_repository.create(venta)
            self.uow.commit()

            created_venta = self.uow.venta_repository.find_by_id(id)
        except:
            self.uow.rollback()
            raise
        return VentaReadModel.from_entity(cast(Venta, created_venta))
