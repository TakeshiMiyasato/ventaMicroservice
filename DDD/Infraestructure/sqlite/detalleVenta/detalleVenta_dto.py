import uuid
from typing import Union

from sqlalchemy import Column, String, Integer, ForeignKey, Float

from DDD.Domain.Model.Venta.detalleVenta import DetalleVenta
from DDD.Infraestructure.ReadModels.detalle_venta_read_model import DetalleVentaReadModel
from DDD.Infraestructure.sqlite.database import Base
from DDD.SharedKernel.ValueObjects.CantidadValid import Cantidad
from DDD.SharedKernel.ValueObjects.TotalValid import Total


class DetalleVentaDTO(Base):
    __tablename__ = 'detalleVentas'
    id: Union[int, Column] = Column(Integer, primary_key=True, autoincrement=True)
    productoId: Union[uuid.UUID, Column] = Column(String, ForeignKey('productos.id'), nullable=False)
    ventaId: Union[uuid.UUID, Column] = Column(String, ForeignKey('ventas.id'), nullable=False)
    cantidad: Union[Cantidad, Column] = Column(Integer, nullable=False)
    subtotal: Union[Total, Column] = Column(Float, nullable=False)

    def to_entity(self) -> DetalleVenta:
        return DetalleVenta(
            id=self.id,
            productoId=self.productoId,
            ventaId=self.ventaId,
            cantidad=self.cantidad,
            subtotal=self.subtotal
        )

    def to_read_model(self) -> DetalleVentaReadModel:
        return DetalleVentaReadModel(
            id=self.id,
            productoId=self.productoId,
            ventaId=self.ventaId,
            cantidad= self.cantidad,
            subtotal=self.subtotal
        )

    @staticmethod
    def from_entity(detalleVenta: DetalleVenta) -> "DetalleVentaDTO":
        return DetalleVentaDTO(
            id=detalleVenta.id,
            productoId=detalleVenta.productoId,
            ventaId=detalleVenta.ventaId,
            cantidad=detalleVenta.cantidad,
            subtotal=detalleVenta.subtotal
        )