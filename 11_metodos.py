# Funciones del lenguaje

# Variable base para los ejemplos
language = "Python"

# --- Ejemplos de Métodos de String ---

print(language.capitalize())  # Pone solo la primera letra en mayúscula (y el resto en minúscula).
print(language.upper())       # Convierte toda la cadena a MAYÚSCULAS.
print(language.count("t"))    # Cuenta cuántas veces aparece la "t" minúscula (distingue may/min).
print(language.isnumeric())   # Comprueba si la cadena es solo numérica (False para "Python").
print("1".isnumeric())        # Comprueba si la cadena es solo numérica (True para "1").
print(language.lower())       # Convierte toda la cadena a minúsculas.
print(language.lower().isupper()) # Convierte a minúsculas ("python") y luego comprueba si está en mayúsculas (False).
print(language.startswith("Py"))  # Comprueba si la cadena empieza exactamente con "Py" (True).
print("Py" == "py")           # Compara si "Py" es exactamente igual a "py" (False, distingue may/min).

#-------------------------------------------------------------------------------------------------------------------------

mi_texto = "Python es Genial"
texto_con_espacios = "   contenido   "
una_lista = [1, "a", True]

print(texto_con_espacios.strip()) # Elimina espacios en blanco (o caracteres) SOLO al inicio y al final.
print(mi_texto.replace("Genial", "Poderoso")) # Reemplaza una parte del string por otra ("Viejo", "Nuevo").
print(mi_texto.find("es"))    # Retorna la posición (índice) donde empieza el texto (Empieza en 0).
print(mi_texto.find("Java"))  # Retorna -1 si no encuentra el texto.
print(len(mi_texto))          # Retorna la longitud (cantidad de caracteres) de un string.
print(len(una_lista))         # Retorna la cantidad de (items o elementos) de una lista.