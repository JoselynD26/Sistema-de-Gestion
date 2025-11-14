from sqlalchemy import Column, Integer, String, Enum
from app.core.config import Base

class Docente(Base):
    __tablename__ = "docente"

    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, nullable=False, index=True)
    correo = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    nombres = Column(String, nullable=False)
    regimen = Column(Enum("LOES", "Codigo de trabajo", name="regimen_enum"), nullable=False)
    observacion = Column(Enum("Medio tiempo", "Tiempo completo", name="observacion_enum"), nullable=False)