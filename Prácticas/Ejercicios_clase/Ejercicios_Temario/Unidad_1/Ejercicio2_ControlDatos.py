# Ejercicio List:
"""
Crea una aplicación en consola donde se permitan gestionar las calificaciones de
la asignatura. Para ello, mediante un menú permite las siguientes acciones:
Programación en Python
Introducir notas: el usuario introducirá notas hasta que meta un -1. Esto
indicará que la introducción ha terminado. Una vez realizado esto volverá a
aparecer el mené.
Listar notas: se mostrarán todas las notas de una en una.
Obtener extremos: se mostrarán la nota más alta y baja.
Obtener información: se mostrarán los siguientes datos sobre las notas: total
introducidas, número suspensos, número aprobador, nota media.

"""

notas = []

# --- 1. Bucle principal (while True) para que el menú sea continuo ---
while True:
    print("\n--- Calificaciones de la Asignatura ---")
    print("1. Introducir notas")
    print("2. Listar notas")
    print("3. Obtener extremos (alta y baja)")
    print("4. Obtener información (media, aprobados, etc.)")
    print("5. Salir")
    print("------------------------------------------")
    
    opcion = input("Selecciona una opción (1-5): ")

    match opcion:
        # --- CASE 1: Introducir Notas (con bucle anidado) ---
        case "1":
            print("\nIntroduce tus notas (0-10). Escribe -1 para terminar.")
            while True:
                try:
                    # Pedimos la nota como texto
                    nota_str = input("Introduce una nota: ")
                    # Convertimos a float (decimal)
                    nota = float(nota_str)

                    if nota == -1:
                        print("...Volviendo al menú principal.")
                        break # Rompe el bucle de "Introducir notas"
                    
                    # Validación de la nota
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        print(f"Nota {nota} añadida. Total: {len(notas)}")
                    else:
                        print("Error: La nota debe estar entre 0 y 10.")
                
                except ValueError:
                    # Si el usuario escribe texto (ej: "hola") en lugar de un número
                    print("Error: Debes introducir un valor numérico.")

        # --- CASE 2: Listar Notas ---
        case "2":
            print("\n--- Listado de Notas ---")
            if not notas: # (Forma corta de 'if len(notas) == 0:')
                print("Aún no hay notas introducidas.")
            else:
                # 'enumerate(notas, 1)' numera la lista empezando en 1
                for i, nota in enumerate(notas, 1):
                    print(f"Nota {i}: {nota}")

        # --- CASE 3: Obtener Extremos ---
        case "3":
            print("\n--- Notas Extremas ---")
            if not notas:
                print("Aún no hay notas introducidas.")
            else:
                # max() y min() fallarían si la lista está vacía
                print(f"La nota MÁS ALTA es: {max(notas)}")
                print(f"La nota MÁS BAJA es: {min(notas)}")

        # --- CASE 4: Obtener Información ---
        case "4":
            print("\n--- Información General ---")
            if not notas:
                print("Aún no hay notas introducidas.")
            else:
                # 1. Total
                total_notas = len(notas)
                print(f"Total de notas introducidas: {total_notas}")

                # 2. Aprobados y Suspensos (Asumiendo 5.0 para aprobar)
                suspensos = 0
                aprobados = 0
                for n in notas:
                    if n < 5:
                        suspensos += 1
                    else:
                        aprobados += 1
                
                print(f"Número de Aprobados (>= 5): {aprobados}")
                print(f"Número de Suspensos (< 5): {suspensos}")

                # 3. Nota Media
                media = sum(notas) / total_notas
                # ':.2f' formatea el número para mostrar solo 2 decimales
                print(f"Nota Media: {media:.2f}")

        # --- CASE 5: Salir ---
        case "5":
            print("¡Hasta pronto!")
            break # Rompe el bucle 'while True' principal y termina

        # --- CASE por defecto (Opción inválida) ---
        case _:
            print("Opción no válida. Por favor, elige del 1 al 5.")