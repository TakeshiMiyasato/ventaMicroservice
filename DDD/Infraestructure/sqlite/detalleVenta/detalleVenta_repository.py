import uuid
from typing import Optional

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from DDD.Domain.Model.Venta.detalleVenta import DetalleVenta
from DDD.Domain.Respositories.ABSdetalleVenta_repository import DetalleVentaRepository
from DDD.Infraestructure.sqlite.detalleVenta.detalleVenta_dto import DetalleVentaDTO
from DDD.Domain.UseCases import \
    DetalleVentaCommandUseCaseUnitOfWork


class DetalleVentaRepositoryImpl(DetalleVentaRepository):
    def __init__(self, session: Session):
        self.session: Session = session

    def create(self, detalleVenta: DetalleVenta):
        detalleVenta_dto = DetalleVentaDTO.from_entity(detalleVenta)
        try:
            self.session.add(detalleVenta_dto)
        except:
            raise

    def find_by_id(self, id: uuid) -> Optional[DetalleVenta]:
        try:
            detalleVenta_dto = self.session.query(DetalleVentaDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return detalleVenta_dto.to_entity()


class DetalleVentaCommandUseCaseUnitOfWorkImpl(DetalleVentaCommandUseCaseUnitOfWork):
    def __init__(self, session: Session, detalleVenta_repository: DetalleVentaRepository):
        self.session: Session = session
        self.detalleVenta_repository: DetalleVentaRepository = detalleVenta_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
