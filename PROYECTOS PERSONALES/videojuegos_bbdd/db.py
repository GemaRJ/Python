import mysql.connector
import os
from dotenv import load_dotenv

# Cargamos las variables del archivo .env
load_dotenv()

def obtener_conexion():
    """
    Crea y devuelve una conexión a la base de datos del club.
    Si ocurre un error, devuelve None.
    """
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "videojuegos"),
            use_pure=True  # ¡Vital para evitar que Python 3.14 se cierre de golpe!
        )
        return conexion

    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None