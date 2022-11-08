from pydantic import BaseModel, Field

from DDD.Domain.ValueObjects.PrecioProductoValid import PrecioProducto
from DDD.Domain.ValueObjects.StockProductoValid import StockProducto


class ProductoWriteModel(BaseModel):
    nombre: str = Field()
    descripcion: str = Field()
    precio: PrecioProducto = Field()
    stock: StockProducto = Field()
