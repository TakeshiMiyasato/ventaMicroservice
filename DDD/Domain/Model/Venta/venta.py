import uuid

from DDD.SharedKernel.Core.ABSEntity import Entity
from DDD.SharedKernel.ValueObjects.TotalValid import Total


class Venta(Entity):
    def __init__(self, id: uuid, total: Total, clienteId: uuid):
        self.id: uuid = id
        self.total: Total = total
        self.clienteId: uuid = clienteId