from sqlalchemy import Column, Integer, String
from app.core.config import Base

class Carrera(Base):
    __tablename__ = "carrera"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)