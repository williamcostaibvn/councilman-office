from typing import List
from fastapi import Depends
from config.database import get_db
from fastapi.routing import APIRouter
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from domain.demanda import demanda_service
from domain.demanda.demanda_schema import DemandSchema, DemandSchemaCreate

router = APIRouter()


@router.get("/",
            summary="Operação responsável por retornar todas as Demandas por filtro.",
            response_model=List[DemandSchema])
def get_demands(db: Session = Depends(get_db)):
    return demanda_service.get_demands(db)


@router.post("/",
             summary="Operação responsável por criar uma nova Demanda.",
             response_model=DemandSchema)
def create_demand(body: DemandSchemaCreate, db: Session = Depends(get_db)):
    return demanda_service.create(db, body)
