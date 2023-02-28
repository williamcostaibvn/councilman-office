from datetime import date
from typing import Optional
from pydantic import BaseModel, Field
from domain.eleitor.eleitor_schema import ElectorSchema


class DemandSchema(BaseModel):
    id: int
    demand_type: str
    register_date: date
    elector_id: Optional[ElectorSchema]
    elector_name: Optional[ElectorSchema]
    demand_details: str
    demand_status: str

    class Config:
        orm_mode = True


class DemandSchemaCreate(BaseModel):
    demand_type: str=Field(..., example="Exemplo: Tapa-Buraco, Extração de Árvore, etc")
    register_date: str=Field(..., example="Exemplo: 25/01/2023")
    elector_id: int=Field(..., example="Exemplo: 2")
    elector_name: str=Field(..., example="Nome do Eleitor")
    demand_details: str=Field(..., example="Descrição do trabalho a ser realizado")
    demand_status: str=Field(..., example="Exemplo: 'Solicitado', 'Em Andamento', 'Concluído'")

    class Config:
        orm_mode = True    
