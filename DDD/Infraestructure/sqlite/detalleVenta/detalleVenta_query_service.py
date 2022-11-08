import uuid
from typing import List

from sqlalchemy.orm import Session

from DDD.Infraestructure.ReadModels.detalle_venta_read_model import DetalleVentaReadModel
from DDD.Infraestructure.sqlite.detalleVenta.detalleVenta_dto import DetalleVentaDTO
from DDD.Domain.UseCases.Query.Venta.ABSDetalleVentaQueryService import DetalleVentaQueryService


class DetalleVentaQueryServiceImpl(DetalleVentaQueryService):
    def __init__(self, session: Session):
        self.session: Session = session

    def find_all_by_id(self, id: uuid.UUID) -> List[DetalleVentaReadModel]:
        try:
            detalleVenta_dtos = (
                self.session.query(DetalleVentaDTO).filter_by(ventaId=id).all()
            )
        except:
            raise
        if len(detalleVenta_dtos) == 0:
            return []
        return list(map(lambda detalleVenta_dto: detalleVenta_dto.to_read_model(), detalleVenta_dtos))
