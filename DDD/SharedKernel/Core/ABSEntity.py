import uuid
from abc import ABC


class Entity(ABC):
    id = uuid.UUID