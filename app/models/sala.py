from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.config import Base

class Sala(Base):
    __tablename__ = "sala"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    tipo = Column(String, default="docentes")
    jornada = Column(String)
    id_sede = Column(Integer, ForeignKey("sede.id"))