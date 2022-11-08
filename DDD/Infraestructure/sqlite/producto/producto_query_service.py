import uuid
from typing import List, Optional

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from DDD.Infraestructure.ReadModels.producto_read_model import ProductoReadModel
from DDD.Infraestructure.sqlite.producto.producto_dto import ProductoDTO
from DDD.Domain.UseCases import ProductoQueryService


class ProductoQueryServiceImpl(ProductoQueryService):
    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: uuid.UUID) -> Optional[ProductoReadModel]:
        try:
            producto_dto = self.session.query(ProductoDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return producto_dto.to_read_model()

    def find_all(self) -> List[ProductoReadModel]:
        try:
            producto_dtos = (
                self.session.query(ProductoDTO).all()
            )
        except:
            raise
        if len(producto_dtos) == 0:
            return []

        return list(map(lambda producto_dto: producto_dto.to_read_model(), producto_dtos))
