from fastapi import FastAPI

from domain.eleitor import eleitor_routes
from domain.demanda import demanda_routes


def setup_routes(app: FastAPI):
    app.include_router(eleitor_routes.router,
                       tags=['eleitor'],
                       prefix="/eleitores")

    app.include_router(demanda_routes.router,
                       tags=['demanda'],
                       prefix="/demandas")
