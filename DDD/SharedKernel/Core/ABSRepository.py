import uuid
from abc import ABC, abstractmethod
from typing import Optional

from DDD.SharedKernel.Core.ABSEntity import Entity


class IRepository(ABC):
    @abstractmethod
    def create(self, object: Entity) -> Optional[Entity]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: uuid.UUID) -> Optional[Entity]:
        raise NotImplementedError