""" 
Crear un programa en Python que:
1. Pida los nombres de varios alumnos.
2. Para cada alumno, permita introducir varias notas.
3. Calcule la media de cada alumno.
4. Indique si está aprobado o suspenso.
5. Muestre un resumen final con todos los alumnos procesados.

 """

print("=== GESTOR DE NOTAS ===")

# Lista principal donde se guardarán los diccionarios de alumnos
alumnos = []

# BUCLE PRINCIPAL: pedir alumnos

while True:
    nombre = input("Introduce el nombre del alumno (o pulsa Enter para finalizar): ")

    # Si el usuario pulsa Enter, se sale del bucle
    if nombre == "":
        break

    # Crear el diccionario del alumno
    alumno = {
        "nombre": nombre,
        "notas": []
    }


    # BUCLE SECUNDARIO: pedir notas

    while True:
        nota = input("Introduce una nota (o pulsa Enter para terminar): ")

        # Si no se escribe nada → dejar de pedir notas
        if nota == "":
            break

        # Validación de que la nota es un número válido
        try:
            nota_float = float(nota)

            # Agregar la nota a la lista del alumno
            alumno["notas"].append(nota_float)

        except ValueError:
            print(" Error: la nota debe ser un número válido. Inténtalo de nuevo.")

    # Guardar el diccionario en la lista principal
    alumnos.append(alumno)


# MOSTRAR RESULTADOS FINALES

print("\n=== RESULTADOS ===")

for alumno in alumnos:
    nombre = alumno["nombre"]
    notas = alumno["notas"]

    # Cálculo de la media (si no tiene notas → media = 0)
    if len(notas) > 0:
        media = sum(notas) / len(notas)
    else:
        media = 0

    # Determinar estado
    if media >= 5:
        estado = "APROBADO"
    else:
        estado = "SUSPENSO"

    # Mostrar resultado con dos decimales
    print(f"{nombre}: media = {media:.2f} -> {estado}")

# Mostrar total de alumnos procesados
print(f"\nTotal de alumnos procesados: {len(alumnos)}")
