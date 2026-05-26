# PROGRAMA: gestion_libros.py
# DESCRIPCIÓN:
# Sistema de gestión de libros de una biblioteca
# Permite:
# - Cargar libros desde un archivo
# - Crear el archivo si no existe
# - Mostrar libros por pantalla

import os  # Librería para comprobar si el archivo existe

# Nombre del archivo donde se guardan los libros
ARCHIVO = "libros.txt"


# FUNCIÓN: crear_archivo_si_no_existe
# DESCRIPCIÓN:
# - Comprueba si el archivo existe
# - Si no existe, lo crea con datos de ejemplo
def crear_archivo_si_no_existe():
    if not os.path.exists(ARCHIVO):
        print("El archivo no existe. Creando archivo con datos por defecto...\n")

        # Creamos el archivo y añadimos libros de ejemplo
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            f.write("Los pilares de la tierra,1049,Mario\n")
            f.write("El nombre de la rosa,2234,Luis\n")
            f.write("El perfume,5678,Ángela\n")


# FUNCIÓN: cargar_libros
# DESCRIPCIÓN:
# - Lee el archivo libros.txt
# - Devuelve una lista de libros
# - Cada libro será un diccionario
def cargar_libros():
    libros = []

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            # Eliminamos saltos de línea y dividimos por comas
            datos = linea.strip().split(",")

            # Comprobamos que la línea tenga exactamente 3 datos
            if len(datos) == 3:
                # Creamos un diccionario por cada libro
                libro = {
                    "nombre": datos[0],
                    "id": datos[1],
                    "encargado": datos[2]
                }

                libros.append(libro)

    return libros


# FUNCIÓN: mostrar_libros
# DESCRIPCIÓN:
# - Imprime todos los libros de forma clara
def mostrar_libros(libros):
    print("=== LISTADO DE LIBROS ===\n")

    for libro in libros:
        print(f"Nombre: {libro['nombre']}")
        print(f"ID: {libro['id']}")
        print(f"Encargado: {libro['encargado']}")
        print("----------------------------")


# PROGRAMA PRINCIPAL
def main():
    # Crear archivo si no existe
    crear_archivo_si_no_existe()

    # Cargar libros desde el archivo
    libros = cargar_libros()

    # Mostrar libros por pantalla
    mostrar_libros(libros)


# Ejecutamos el programa
if __name__ == "__main__":
    main()





