from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.config import SessionLocal
from app.schemas.docente_materia import DocenteMateriaCreate, DocenteMateriaOut, DocenteMateriaUpdate
from app.crud.docente_materia import listar_relaciones, obtener_relacion, actualizar_relacion, eliminar_relacion
from app.crud.docente_materia import crear_relacion

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/docente-materia/")
def crear_docente_materia(relacion: DocenteMateriaCreate, db: Session = Depends(get_db)):
    return crear_relacion(db, relacion)

# Listar todas las relaciones
@router.get("/docente-materia/", response_model=list[DocenteMateriaOut])
def listar_docente_materia(db: Session = Depends(get_db)):
    return listar_relaciones(db)


# Obtener relación por ID
@router.get("/docente-materia/{relacion_id}", response_model=DocenteMateriaOut)
def obtener_docente_materia(relacion_id: int, db: Session = Depends(get_db)):
    return obtener_relacion(db, relacion_id)


# Actualizar relación Docente-Materia (PUT)
@router.put("/docente-materia/{relacion_id}", response_model=DocenteMateriaOut)
def actualizar_docente_materia(relacion_id: int, data: DocenteMateriaUpdate, db: Session = Depends(get_db)):
    relacion = actualizar_relacion(db, relacion_id, data)
    if relacion:
        return relacion
    return {"mensaje": "Relación docente-materia no encontrada"}


# Eliminar relación
@router.delete("/docente-materia/{relacion_id}")
def eliminar_docente_materia(relacion_id: int, db: Session = Depends(get_db)):
    relacion = eliminar_relacion(db, relacion_id)
    if relacion:
        return {"mensaje": "Relación eliminada correctamente"}
    return {"mensaje": "Relación no encontrada"}