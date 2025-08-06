def analizar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

            print("Contenido del archivo:")
            print("----------------------")
            print(contenido)
            print("----------------------")

            # Contar palabras
            palabras = contenido.split()
            num_palabras = len(palabras)

            # Contar letras (solo alfabéticas)
            letras = [c for c in contenido if c.isalpha()]
            num_letras = len(letras)

            print(f"Número total de palabras: {num_palabras}")
            print(f"Número total de letras: {num_letras}")

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Llamar a la función con el nombre del archivo
analizar_archivo("C:/Users/gr/Python/03_Ejercicio/ejercicio3.txt")
