from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.config import Base

class Escritorio(Base):
    __tablename__ = "escritorio"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True, nullable=False)
    id_sala = Column(Integer, ForeignKey("aula.id"))
    id_carrera = Column(Integer, ForeignKey("carrera.id"))
    id_docente = Column(Integer, ForeignKey("docente.id"), nullable=True)