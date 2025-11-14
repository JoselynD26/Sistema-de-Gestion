# Sistema Académico — API REST

API desarrollada con FastAPI para la gestión académica institucional. Protegida con JWT y control de roles.

## Instalación

```bash
git clone https://github.com/JoselynD26/Sistema-de-Gestion.git
cd Sistema-de-Gestion
pip install -r requirements.txt

## Activar entirno virtual
python -m venv venv
venv\Scripts\activate 

## Crear base de datos
python create_tables.py  

## Ejecutar la aplicacion
uvicorn app.main:app --reload
