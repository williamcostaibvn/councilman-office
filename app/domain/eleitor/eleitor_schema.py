from datetime import datetime
from pydantic import BaseModel, Field


class ElectorSchema(BaseModel):
    id: int
    elector_name: str=Field(..., example="João da Silva")
    born_date: str
    cpf_number: str
    elector_register: str
    zone_number: str
    section_number: str
    mother_name: str
    email: str
    phone_number: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ElectorSchemaCreate(BaseModel):
    id: int
    elector_name: str
    born_date: str
    cpf_number: str
    elector_register: str
    zone_number: str
    section_number: str
    mother_name: str
    email: str
    phone_number: str

    class Config:
        orm_mode = True    
