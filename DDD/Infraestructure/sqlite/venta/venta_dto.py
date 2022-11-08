import uuid
from datetime import datetime
from typing import Union

from sqlalchemy import Column, Float, String

from DDD.Domain.Model.Venta.venta import Venta
from DDD.Infraestructure.ReadModels.venta_read_model import VentaReadModel
from DDD.Infraestructure.sqlite.database import Base
from DDD.SharedKernel.ValueObjects.TotalValid import Total


class VentaDTO(Base):
    __tablename__ = 'ventas'
    id: Union[uuid.UUID, Column] = Column(String, primary_key=True, autoincrement=False)
    total: Union[Total, Column] = Column(Float, nullable=False)
    clienteId: Union[uuid.UUID, Column] = Column(String, nullable=False)

    def to_entity(self) -> Venta:
        return Venta(
            id=self.id,
            total=self.total,
            clienteId=self.clienteId,
        )

    def to_read_model(self) -> VentaReadModel:
        return VentaReadModel(
            id=self.id,
            total=self.total,
            clienteId=self.clienteId,
        )

    @staticmethod
    def from_entity(venta: Venta) -> "VentaDTO":
        return VentaDTO(
            id=venta.id,
            total=venta.total,
            clienteId=venta.clienteId,
        )
