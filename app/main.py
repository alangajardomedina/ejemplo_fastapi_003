#importamos la librería para crear la API
from fastapi import FastAPI

#Vamos a crear una variable para la API:
api = FastAPI()

#Vamos a crear los endpoints de la API:
@api.get("/")
def root():
    return {"mensaje": "Bienvenido desde API 2"}

@api.get("/{id}")
def obtener_usuario(id: int):
    usuarios = {
        1: {"nombre": "Lalo", "apellido": "Cura"},
        2: {"nombre": "Elsa", "apellido": "Pato"},
        3: {"nombre": "Armando", "apellido": "Casas"}
    }
    return usuarios.get(id)
