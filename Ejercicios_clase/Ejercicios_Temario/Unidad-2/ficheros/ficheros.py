def leer_notas():
    try:
        # Abrimos el fichero en modo lectura
        with open("notas.txt", "r", encoding="utf-8") as fichero:
            
            for linea in fichero:
                linea = linea.strip()  # Eliminamos espacios y saltos de línea
                
                # Saltar líneas vacías
                if not linea:
                    continue

                partes = linea.split(",")

                # Verificar que tenga exactamente 2 partes
                if len(partes) != 2:
                    print(f"Línea con formato incorrecto: {linea}")
                    continue

                nombre, nota = partes

                try:
                    nota = float(nota)
                    print(f"Alumno: {nombre} - Nota: {nota}")
                except ValueError:
                    print(f"Alumno: {nombre} - Nota inválida: {nota}")

    except FileNotFoundError:
        print("Error: El fichero 'notas.txt' no existe en esta carpeta.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


# Llamada a la función
leer_notas()