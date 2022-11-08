import uuid

from pydantic import BaseModel, Field

from DDD.Domain.Model.Venta.detalleVenta import DetalleVenta
from DDD.SharedKernel.ValueObjects.CantidadValid import Cantidad
from DDD.SharedKernel.ValueObjects.TotalValid import Total


class DetalleVentaReadModel(BaseModel):
    id: uuid.UUID = Field()
    productoId: uuid.UUID = Field()
    ventaId: uuid.UUID = Field()
    cantidad: Cantidad = Field()
    subtotal: Total = Field()

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(detalleVenta: DetalleVenta) -> "DetalleVentaReadModel":
        return DetalleVentaReadModel(
            id=detalleVenta.id,
            productoId=detalleVenta.productoId,
            ventaId=detalleVenta.ventaId,
            cantidad=detalleVenta.cantidad,
            subtotal=detalleVenta.subtotal
        )