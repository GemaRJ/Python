import mysql.connector  # Conector oficial de MySQL para Python
import os               # Permite acceder a variables del sistema
from dotenv import load_dotenv # Carga las variables de entorno desde un archivo .env
from sqlite3 import connect # Conector para SQLite

load_dotenv()

def connect_mysql():
    """Establece una conexión a la base de datos MySQL utilizando las variables de entorno."""
    try:
        conexion = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )
        print("Conexión a MySQL exitosa")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a MySQL: {err}")
        return conexion

def connect_sqlite():
    """Establece una conexión a la base de datos SQLite."""
    try:
        connection = connect(os.getenv('SQLITE_DB'))
        print("Conexión a SQLite exitosa")
        return connection
    except Exception as err:
        print(f"Error al conectar a SQLite: {err}")
        return None