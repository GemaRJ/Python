"""  Leer todas las líneas y procesarlas una a una.
▪ Para cada línea
o Separar el nombre y la nota.
o Intentar convertir la nota a float.
o Si la conversión falla (por ejemplo, si aparece mal en lugar de una nota válida),
capturar la excepción y mostrar un mensaje de aviso con el nombre del
alumno.
▪ Escribir en un nuevo fichero llamado notas_validas.txt solo las líneas con notas
válidas.
Durante el programa debes utilizar bloques try-except para controlar los posibles
errores (como errores de conversión o si el fichero original no existe). """

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