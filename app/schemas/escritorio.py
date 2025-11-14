from pydantic import BaseModel

class EscritorioCreate(BaseModel):
    codigo: str
    id_sala: int
    id_carrera: int
    id_docente: int | None = None

class EscritorioOut(EscritorioCreate):
    id: int

    class Config:
        from_attributes = True