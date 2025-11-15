""" Crea una aplicación en consola donde se permitan gestionar las calificaciones de
la asignatura. Para ello, mediante un menú permite las siguientes acciones:
Introducir notas: el usuario introducirá notas hasta que meta un -1. Esto
indicará que la introducción ha terminado. Una vez realizado esto volverá a
aparecer el mené.
o Listar notas: se mostrarán todas las notas de una en una.
o Obtener extremos: se mostrarán la nota más alta y baja.
o Obtener información: se mostrarán los siguientes datos sobre las notas: total
introducidas, número suspensos, número aprobador, nota media.
"""
# gestor_notas_profesor_final.py
# Este es el código completo que se deduce de TODAS las imágenes.

print("=== GESTOR DE NOTAS ===")

# Lista principal que guardará todos los alumnos
alumnos = []

# --- FASE 1: INTRODUCCIÓN DE DATOS ---
# (Basado en las imágenes 2 y 3)

# Bucle exterior para los alumnos
while True:
    nombre = input("Introduce el nombre del alumno (o pulsa Enter para finalizar): ")
    if nombre == "":
        break # Termina de pedir alumnos
    
    # Bucle interior para las notas de ESE alumno
    notas = []
    print(f"Introduce las notas para {nombre}:")
    
    while True:
        nota = input("  Introduce una nota (o pulsa Enter para terminar): ")
        if nota == "":
            break # Termina de pedir notas para este alumno
        
        # Intenta convertir la nota a número y añadirla a la lista 'notas'
        try:
            notas.append(float(nota))
        except ValueError:
            print("  (Error: Por favor, introduce un número válido.)")
    
    # Guardar el alumno en la lista principal
    # (Esto se ejecuta cuando se rompe el bule de notas)
    alumno = {"nombre": nombre, "notas": notas}
    alumnos.append(alumno)
    print(f"-> Alumno {nombre} guardado.")


# --- FASE 2: CÁLCULO DE RESULTADOS ---
# (Basado en las imágenes 4 y 5 - la última que enviaste)

print("\n=== RESULTADOS ===")

# Recorrer la lista de alumnos para imprimir sus datos
for alumno in alumnos:
    
    # Comprobar si el alumno tiene notas para evitar dividir por cero
    if len(alumno["notas"]) > 0:
        media = sum(alumno["notas"]) / len(alumno["notas"])
    else:
        # Si no hay notas, la media es 0
        media = 0.0 
    
    # Determinar el estado (Aprobado/Suspenso) - ¡NUEVO!
    estado = "APROBADO" if media >= 5 else "SUSPENSO"
    
    # Imprimir el resumen por alumno (Formato actualizado) - ¡NUEVO!
    print(f"{alumno['nombre']}: media = {media:.2f} -> {estado}")


# --- RESUMEN FINAL ---
# (Basado en la última imagen)

print("\n--- Fin del programa ---")
print(f"Se han procesado {len(alumnos)} alumnos.")