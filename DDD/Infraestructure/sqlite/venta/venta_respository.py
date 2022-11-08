import uuid
from typing import Optional

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from DDD.Domain.UseCases.Command.ABSVentaCommandUseCaseUnitOfWork import VentaCommandUseCaseUnitOfWork
from DDD.Domain.Respositories.ABSventa_repository import VentaRepository
from DDD.Domain.Model.Venta.venta import Venta
from DDD.Infraestructure.sqlite.venta.venta_dto import VentaDTO


class VentaRepositoryImpl(VentaRepository):
    def __init__(self, session: Session):
        self.session: Session = session

    def create(self, venta: Venta):
        venta_dto = VentaDTO.from_entity(venta)
        try:
            self.session.add(venta_dto)
        except:
            raise

    def find_by_id(self, id: uuid) -> Optional[Venta]:
        try:
            venta_dto = self.session.query(VentaDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return venta_dto.to_entity()


class VentaCommandUseCaseUnitOfWorkImpl(VentaCommandUseCaseUnitOfWork):
    def __init__(self, session: Session, venta_repository: VentaRepository):
        self.session: Session = session
        self.venta_repository: VentaRepository = venta_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
