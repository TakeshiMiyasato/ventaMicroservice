import uuid
from typing import Optional, List

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from DDD.Domain.UseCases.Query.Venta.ABSVentaQueryService import VentaQueryService
from DDD.Infraestructure.ReadModels.venta_read_model import VentaReadModel
from DDD.Infraestructure.sqlite.venta.venta_dto import VentaDTO


class VentaQueryServiceImpl(VentaQueryService):
    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_venta_id(self, id: uuid) -> Optional[VentaReadModel]:
        try:
            ventas_dto = self.session.query(VentaDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return ventas_dto.to_read_model()

    def find_all_by_clienteId(self, clienteId: uuid) -> List[VentaReadModel]:
        try:
            venta_dtos = (
                self.session.query(VentaDTO).filter_by(clienteId = clienteId).all()
            )
        except:
            raise

        if len(venta_dtos) == 0:
            return []

        return list(map(lambda venta_dto: venta_dto.to_read_model(), venta_dtos))