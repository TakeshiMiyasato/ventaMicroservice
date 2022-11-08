import uuid

from pydantic import BaseModel, Field

from DDD.SharedKernel.ValueObjects.CantidadValid import Cantidad
from DDD.SharedKernel.ValueObjects.TotalValid import Total


class DetalleVentaWriteModel(BaseModel):
    productoId: uuid.UUID = Field()
    ventaId: uuid.UUID = Field()
    cantidad: Cantidad = Field()
    subtotal: Total = Field()
