from typing import List
from fastapi import Depends
from fastapi.routing import APIRouter
from config.database import get_db
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from domain.eleitor import eleitor_service
from domain.eleitor.eleitor_schema import ElectorSchema, ElectorSchemaCreate

router = APIRouter()


@router.get("/",
            summary="Operação responsável por retornar todos os eleitores cadastrados.",
            response_model=List[ElectorSchema])
def get_electors(db: Session = Depends(get_db)):
    return eleitor_service.get_electors(db)

@router.get("/{id}",
            summary="Operação responsável por retornar um eleitor.",
            response_model=List[ElectorSchema])
def get_elector(id: int, db: Session = Depends(get_db)):
    return eleitor_service.get_elector(db, id)

@router.post("/",
             summary="Operação responsável por cadastrar novo eleitor.",
             response_model=ElectorSchema)
def create_elector(body: ElectorSchemaCreate, db: Session = Depends(get_db)):
    return eleitor_service.create(db, body)

@router.delete("/{id}",
            summary="Operação responsável por apagar o cadastro de um eleitor.",
            response_model=List[ElectorSchema])
def delete_elector(id: int, db: Session = Depends(get_db)):
    return eleitor_service.delete(db, id)
