from typing import Iterator

from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

from DDD.Domain.Respositories.ABSproducto_repository import ProductoRepository
from DDD.Domain.Respositories.ABSventa_repository import VentaRepository
from DDD.Infraestructure.sqlite import VentaQueryServiceImpl
from DDD.Infraestructure.sqlite.producto.producto_query_service import ProductoQueryServiceImpl
from DDD.Infraestructure.sqlite.producto.producto_repository import ProductoRepositoryImpl, \
    ProductoCommandUseCaseUnitOfWorkImpl
from DDD.Infraestructure.sqlite.venta.venta_respository import VentaCommandUseCaseUnitOfWorkImpl, VentaRepositoryImpl
from DDD.Domain.UseCases import ProductoCommandUseCase, \
    ProductoCommandUseCaseUnitOfWork, ProductoCommandUseCaseImpl
from DDD.Domain.UseCases import VentaCommandUseCase, \
    VentaCommandUseCaseUnitOfWork, VentaCommandUseCaseImpl
from DDD.Domain.UseCases import ProductoQueryService
from DDD.Domain.UseCases.Query.Producto.ABSProductoQueryUseCase import ProductoQueryUseCase, \
    ProductoQueryUseCaseImpl
from DDD.Domain.UseCases.Query.Venta.ABSVentaQueryService import VentaQueryService
from DDD.Domain.UseCases.Query.Venta.ABSVentaQueryUseCase import VentaQueryUseCase, VentaQueryUseCaseImpl
from DDD.Infraestructure.sqlite.database import create_tables, SessionLocal

app = FastAPI()

create_tables()


def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def venta_query_usecase(session: Session = Depends(get_session)) -> VentaQueryUseCase:
    venta_query_service: VentaQueryService = VentaQueryServiceImpl(session)
    return VentaQueryUseCaseImpl(venta_query_service)


def venta_command_usecase(session: Session = Depends(get_session)) -> VentaCommandUseCase:
    venta_repository: VentaRepository = VentaRepositoryImpl(session)
    uow: VentaCommandUseCaseUnitOfWork = VentaCommandUseCaseUnitOfWorkImpl(
        session, venta_repository=venta_repository
    )
    return VentaCommandUseCaseImpl(uow)


def producto_query_usecase(session: Session = Depends(get_session)) -> ProductoQueryUseCase:
    producto_query_service: ProductoQueryService = ProductoQueryServiceImpl(session)
    return ProductoQueryUseCaseImpl(producto_query_service)


def producto_command_usecase(session: Session = Depends(get_session)) -> ProductoCommandUseCase:
    producto_repository: ProductoRepository = ProductoRepositoryImpl(session)
    uow: ProductoCommandUseCaseUnitOfWork = ProductoCommandUseCaseUnitOfWorkImpl(
        session, producto_repository=producto_repository
    )
    return ProductoCommandUseCaseImpl(uow)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
