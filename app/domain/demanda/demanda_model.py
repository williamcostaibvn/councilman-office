from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.types import Date
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import (Column, Integer, String, ForeignKey)


class Demanda(Base):
    __tablename__ = "demandas"

    id = Column(Integer, primary_key=True, index=True)
    demand_type = Column(String, nullable=False)
    register_date = Column(Date)
    elector_id = Column(Integer,  ForeignKey("eleitores.id"))
    elector_name = relationship("Eleitor", backref="eleitores.elector_name", uselist=False)
    demand_details = Column(String, nullable=False)
    demand_status = Column(String, nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.demand_type}, {self.elector_name}, {self.demand_details}, {self.demand_status}"
