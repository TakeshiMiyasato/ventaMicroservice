import uuid

from pydantic import BaseModel, Field

from DDD.Domain.Model.Producto.producto import Producto
from DDD.Domain.ValueObjects.PrecioProductoValid import PrecioProducto
from DDD.Domain.ValueObjects.StockProductoValid import StockProducto


class ProductoReadModel(BaseModel):
    id: uuid.UUID = Field(example='vytxeTZskVKR7C7WgdSP3d')
    nombre: str = Field(example='Carne')
    descripcion: str = Field(example='Humana')
    precio: PrecioProducto = Field(example=35.0)
    stock: StockProducto = Field(example=10)

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(producto: Producto) -> "ProductoReadModel":
        return ProductoReadModel(
            id=producto.id,
            nombre=producto.nombre,
            descripcion=producto.descripcion,
            precio=producto.precio,
            stock=producto.stock
        )
