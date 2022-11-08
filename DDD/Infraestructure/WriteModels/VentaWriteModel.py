import uuid

from pydantic import BaseModel, Field


class VentaWriteModel(BaseModel):
    total: float = Field(example=200.20)
    clienteId: uuid.UUID = Field(example= 'vytxeTZskBKR7C7WgdSP3d')
    detalle: list = Field(example=
    [
        {
            'productoId': 'vytxeTZskBKR7C7WgdSP3d',
            'cantidad': 10,
            'subtotal': 200.20
        }
    ])