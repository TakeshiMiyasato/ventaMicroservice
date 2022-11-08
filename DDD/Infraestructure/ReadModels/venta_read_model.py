import uuid

from pydantic import Field, BaseModel

from DDD.Domain.Model.Venta.venta import Venta


class VentaReadModel(BaseModel):
    id: uuid.UUID = Field(example='vytxeTZskVKR7C7WgdSP3d')
    total: float = Field(example=200.20)
    clienteId: uuid.UUID = Field(example='vytxeTZskBKR7C7WgdSP3d')

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(venta: Venta) -> "VentaReadModel":
        return VentaReadModel(
            id=venta.id,
            total=venta.total,
            clienteId=venta.clienteId,
        )
