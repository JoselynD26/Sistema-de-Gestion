from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.config import Base

class Materia(Base):
    __tablename__ = "materia"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    id_sede = Column(Integer, ForeignKey("sede.id"))