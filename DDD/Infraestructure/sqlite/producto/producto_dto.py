import uuid
from typing import Union

from sqlalchemy import Column, String, Float, Integer

from DDD.Domain.Model.Producto.producto import Producto
from DDD.Domain.ValueObjects.PrecioProductoValid import PrecioProducto
from DDD.Domain.ValueObjects.StockProductoValid import StockProducto
from DDD.Infraestructure.ReadModels.producto_read_model import ProductoReadModel
from DDD.Infraestructure.sqlite.database import Base


class ProductoDTO(Base):
    __tablename_ = 'productos'
    id: Union[uuid.UUID, Column] = Column(String, primary_key=True, autoincrement=False)
    nombre: Union[str, Column] = Column(String, nullable=False)
    descripcion: Union[str, Column] = Column(String, nullable=False)
    precio: Union[PrecioProducto, Column] = Column(Float, nullable=False)
    stock: Union[StockProducto, Column] = Column(Integer, nullable=False)

    def to_entity(self) -> Producto:
        return Producto(
            id=self.id,
            nombre=self.nombre,
            descripcion=self.descripcion,
            precio=self.precio,
            stock=self.stock
        )

    def to_read_model(self) -> ProductoReadModel:
        return ProductoReadModel(
            id=self.id,
            nombre=self.nombre,
            descripcion=self.descripcion,
            precio=self.precio,
            stock=self.stock
        )

    @staticmethod
    def from_entity(producto: Producto) -> "ProductoDTO":
        return ProductoDTO(
            id=producto.id,
            nombre=producto.nombre,
            descripcion=producto.descripcion,
            precio=producto.precio,
            stock=producto.stock
        )
