import uuid

from DDD.SharedKernel.Core.ABSEntity import Entity
from DDD.SharedKernel.ValueObjects.CantidadValid import Cantidad
from DDD.SharedKernel.ValueObjects.TotalValid import Total


class DetalleVenta(Entity):
    def __init__(self, id:int, productoId: uuid.UUID, ventaId: uuid.UUID, cantidad: Cantidad, subtotal: Total):
        self.id: int = id
        self.productoId: uuid.UUID = productoId
        self.ventaId: uuid.UUID = ventaId
        self.cantidad: Cantidad = cantidad
        self.subtotal: Total = subtotal
