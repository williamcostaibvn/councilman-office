from config.database import Base
from sqlalchemy.types import Date
from sqlalchemy import Column, Integer, String

class Eleitor(Base):
    __tablename__ = "eleitores"

    id = Column(Integer, primary_key=True, index=True)
    elector_name = Column(String, nullable=False)
    born_date = Column(Date)
    cpf_number = Column(String, nullable=False)
    elector_register = Column(String, nullable=False)
    zone_number = Column(String, nullable=False)
    section_number = Column(String, nullable=False)
    mother_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"{self.elector_name}, {self.born_date}, {self.cpf_number}, {self.elector_register}, {self.zone_number}, {self.section_number}, {self.mother_name},  {self.email}, {self.phone_number}"
