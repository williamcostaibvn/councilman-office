import json
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from domain.eleitor.eleitor_model import Eleitor
from domain.demanda.demanda_model import Demanda
from domain.demanda.demanda_repository import DemandRepository
from domain.demanda.demanda_schema import DemandSchema, DemandSchemaCreate


def create(db: Session, body: DemandSchemaCreate) -> DemandSchema:
    elector_id = int(body.elector_id)
    elector = DemandRepository().filter_by_id(db, Eleitor, elector_id)
    if not elector:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Deve existir um eleitor para criar a Demanda")
    

    demand = Demanda(**body.dict())
    print(demand)
    return DemandRepository().create(db, demand)


def get_demands(db: Session) -> DemandSchema:
    return DemandRepository().all(db, Demanda)
