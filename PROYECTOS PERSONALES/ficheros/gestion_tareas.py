# PROGRAMA: gestion_tareas.py
# DESCRIPCIÓN:
# Sistema de gestión de tareas de una asesoría financiera.
# Permite:
# - Leer las tareas desde un archivo de texto
# - Crear el archivo si no existe
# - Mostrar las tareas por pantalla

import os  # Librería para comprobar si el archivo existe

# Nombre del archivo donde se guardan las tareas
ARCHIVO = "tareas.txt"


# FUNCIÓN: crear_archivo_si_no_existe
# DESCRIPCIÓN:
# Comprueba si el archivo existe.
# Si no existe, lo crea con datos de ejemplo.
def crear_archivo_si_no_existe():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            f.write("Preparar balance trimestral,1001,Ana\n")
            f.write("Revisar facturas pendientes,1002,Luis\n")
            f.write("Actualizar datos de clientes,1003,Marta\n")


# FUNCIÓN: cargar_tareas
# DESCRIPCIÓN:
# Lee las tareas desde el archivo de texto.
# Devuelve una lista de tareas.
def cargar_tareas():
    tareas = []

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            datos = linea.strip().split(",")

            if len(datos) == 3:
                tarea = {
                    "nombre": datos[0],
                    "id_tarea": datos[1],
                    "persona_asignada": datos[2]
                }

                tareas.append(tarea)

    return tareas


# FUNCIÓN: mostrar_tareas
# DESCRIPCIÓN:
# Muestra por pantalla todas las tareas
def mostrar_tareas(tareas):
    print("=== LISTADO DE TAREAS ===\n")

    for tarea in tareas:
        print(f"Nombre: {tarea['nombre']}")
        print(f"ID: {tarea['id_tarea']}")
        print(f"Persona asignada: {tarea['persona_asignada']}")
        print("----------------------------")


# PROGRAMA PRINCIPAL
def main():
    crear_archivo_si_no_existe()
    tareas = cargar_tareas()
    mostrar_tareas(tareas)


# Ejecutar el programa
if __name__ == "__main__":
    main()