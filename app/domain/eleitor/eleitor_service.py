from sqlalchemy.orm.session import Session
from domain.eleitor.eleitor_model import Eleitor
from domain.eleitor.eleitor_repository import ElectorRepository
from domain.eleitor.eleitor_schema import ElectorSchema, ElectorSchemaCreate


def create(db: Session, body: ElectorSchemaCreate) -> ElectorSchema:
    elector = Eleitor(**body.dict())
    return ElectorRepository().create(db, elector)


def get_electors(db: Session) -> ElectorSchema:
    return ElectorRepository().all(db, Eleitor)


def get_elector(db: Session, id: int) -> ElectorSchema:
    return ElectorRepository().filter_by_id(db, Eleitor, id)


def delete(db: Session, id: int) -> ElectorSchema:
    return ElectorRepository().delete(db, Eleitor, id)
