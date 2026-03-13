import mysql.connector
import os
from db import obtener_conexion

# CLASES DE OBJETOS 

class Socio:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo



# FUNCIONES CRUD
def crear_tabla():
    """Crea la base de datos y las tablas de socios y videojuegos"""
    try:
        # Nos conectamos al servidor general para crear la BD si no existe
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            use_pure=True # Evita el cierre brusco en Python 3.14
        )
        cursor = conexion.cursor()
        nombre_db = os.getenv("DB_NAME", "videojuegos")
        
        # Creamos la BD y la seleccionamos
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_db}")
        cursor.execute(f"USE {nombre_db}")
        
        # 1. Tabla videojuegos (Se crea primero porque los socios dependen de ella)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS videojuegos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(100) NOT NULL,
            genero VARCHAR(50)
        )
        """)
        
        # 2. Tabla socios (Con clave foránea hacia videojuegos)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS socios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            correo VARCHAR(100) UNIQUE NOT NULL,
            juego_favorito_id INT,
            FOREIGN KEY (juego_favorito_id) REFERENCES videojuegos(id) ON DELETE SET NULL
        )
        """)
        conexion.commit()
        print("Base de datos y tablas (socios y videojuegos) creadas correctamente.")
        
    except mysql.connector.Error as error:
        print("Error al crear las tablas:", error)
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals() and conexion.is_connected(): conexion.close()


def insertar_socios():
    """Inserta un nuevo socio usando la clase Socio"""
    print("\n--- NUEVO SOCIO ---")
    nombre = input("Nombre del socio: ")
    correo = input("Correo electrónico: ")
    
    # Creamos el objeto instanciando la clase
    nuevo_socio = Socio(nombre, correo)
    
    conexion = obtener_conexion()
    if conexion is None: return
    cursor = conexion.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO socios (nombre, correo) VALUES (%s, %s)", 
            (nuevo_socio.nombre, nuevo_socio.correo)
        )
        conexion.commit()
        print("Socio insertado correctamente.")
    except mysql.connector.Error as error:
        print("Error al insertar (¿Quizás el correo ya existe?):", error)
    finally:
        cursor.close()
        conexion.close()


def mostrar_socios():
    """Muestra todos los socios y su videojuego favorito si lo tienen"""
    conexion = obtener_conexion()
    if conexion is None: return
    cursor = conexion.cursor()
    
    # Usamos LEFT JOIN para mostrar el nombre del juego en vez del número de ID
    cursor.execute("""
        SELECT s.id, s.nombre, s.correo, v.titulo 
        FROM socios s
        LEFT JOIN videojuegos v ON s.juego_favorito_id = v.id
    """)
    resultados = cursor.fetchall()
    
    print("\n--- LISTADO DE SOCIOS ---")
    if not resultados:
        print("Todavía no hay socios registrados.")
    
    for fila in resultados:
        id_socio, nombre, correo, juego = fila
        juego_texto = juego if juego else "Ninguno asignado"
        print(f"[{id_socio}] {nombre} - {correo} | Favorito: {juego_texto}")
        
    cursor.close()
    conexion.close()


def actualizar_socio():
    """Actualiza el nombre de un socio buscando por su correo"""
    print("\n--- ACTUALIZAR SOCIO ---")
    correo_actual = input("Introduce el correo del socio a actualizar: ")
    nuevo_nombre = input("Introduce el nuevo nombre: ")
    
    conexion = obtener_conexion()
    if conexion is None: return
    cursor = conexion.cursor()
    
    cursor.execute(
        "UPDATE socios SET nombre = %s WHERE correo = %s", 
        (nuevo_nombre, correo_actual)
    )
    conexion.commit()
    
    if cursor.rowcount > 0:
        print("Datos del socio actualizados correctamente.")
    else:
        print("No se encontró ningún socio con ese correo.")
        
    cursor.close()
    conexion.close()


def eliminar_socio():
    """Elimina un socio buscando por su correo"""
    print("\n--- ELIMINAR SOCIO ---")
    correo = input("Introduce el correo del socio a eliminar: ")
    
    conexion = obtener_conexion()
    if conexion is None: return
    cursor = conexion.cursor()
    
    cursor.execute("DELETE FROM socios WHERE correo = %s", (correo,))
    conexion.commit()
    
    if cursor.rowcount > 0:
        print("Socio eliminado correctamente.")
    else:
        print("No se encontró ningún socio con ese correo.")
        
    cursor.close()
    conexion.close()