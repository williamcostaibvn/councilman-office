from typing import Any
from sqlalchemy.orm.session import Session


class BaseRepository():
    def create(self, db: Session, model: Any) -> Any:
        db.add(model)
        db.commit()
        db.refresh(model)
        return model

    def all(self, db: Session, cls) -> Any:
        return db.query(cls).all()

    def filter_by_id(self, db: Session, cls, id: int) -> Any:
        return db.query(cls).filter(cls.id == id).all()

    def delete(self, db: Session, ) -> Any:
        return db.query(cls).delete(cls.id == id).all()