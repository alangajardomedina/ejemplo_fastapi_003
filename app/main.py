#importamos la librería para crear la API
from fastapi import FastAPI, HTTPException
import cx_Oracle

#Vamos a crear una variable para la API:
api = FastAPI()

#VAMOS A REALIZAR UNA CONEXIÓN CON ORACLE:
def get_conexion():
    try:
        dsn = cx_Oracle.makedsn(
            "localhost",
            1521,
            service_name="orcl.duoc.com.cl"
        )
        conexion = cx_Oracle.connect(
            user="ejemplo_fastapi",
            password="ejemplo_fastapi",
            dsn=dsn
        )
        return conexion
    except Exception as e:
        print("Error al conectar con oracle:",e)
        raise

#Método get que rescata los usuarios:
@api.get("/usuarios")
def get_usuarios():
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("SELECT rut, nombre, email FROM usuario")
        rows = cursor.fetchall()
        lista = []
        for row in rows:
            usu = {
                "rut": row[0],
                "nombre": row[1],
                "email": row[2]
            }
            lista.append(usu)
        return lista
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener usuarios: {str(e)}"
        )
    finally:
        if 'cone' in locals():
            cone.close()
        if 'cursor' in locals():
            cursor.close()