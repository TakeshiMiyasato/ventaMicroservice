import uuid

from DDD.Domain.ValueObjects.PrecioProductoValid import PrecioProducto
from DDD.Domain.ValueObjects.StockProductoValid import StockProducto
from DDD.SharedKernel.Core.ABSEntity import Entity


class Producto(Entity):
    def __init__(self, id: uuid.UUID, nombre: str, descripcion: str, precio: PrecioProducto, stock: StockProducto):
        self.id: uuid.UUID = id
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.precio: PrecioProducto = precio
        self.stock: StockProducto = stock
