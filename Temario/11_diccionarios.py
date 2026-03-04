### 2.3. Diccionarios ###
# Un diccionario es una estructura de datos que almacena pares "clave: valor".
# Son mutables (se pueden cambiar) y ordenados por inserción (desde Python 3.7).
# Las claves deben ser únicas e inmutables (ej. strings, números, tuplas).
# Se definen usando llaves {}.

# --- 1. Definición ---
my_dict = dict() # Crea un diccionario vacío con constructor
my_dict = {}     # Crea un diccionario vacío con literal (preferido)

# Inicialización con datos (el 'trabajador' de los ejemplos)
trabajador = {
    "nombre": "Gema",
    "edad": 37,
    "titulación": "Ingeniería",
    "conocimientos": ["Python", "SQL", "Git"]
}
print(f"Diccionario inicial: {trabajador}")
print(f"Tipo de dato: {type(trabajador)}") # Imprime <class 'dict'>

# --- 2. Acceso a elementos ---
# Para acceder a un elemento se utiliza la clave asociada.
print(f"Acceso con ['nombre']: {trabajador['nombre']}")

# Si la clave no existe, usar [] da un 'KeyError'.
# Es más seguro usar el método .get(), que devuelve None si no la encuentra.
print(f"Acceso con .get('edad'): {trabajador.get('edad')}")
print(f"Acceso a clave inexistente: {trabajador.get('salario')}") # Devuelve None

# Comprobar si una clave existe (antes de acceder)
print(f"¿Existe la clave 'edad'?: {'edad' in trabajador}") # True

# --- 3. Modificar elementos ---
# Muy similar al acceso, indicando el nuevo valor.
print(f"Edad actual: {trabajador['edad']}")
trabajador["edad"] = trabajador["edad"] + 1 # (O trabajador["edad"] += 1)
print(f"Edad modificada: {trabajador['edad']}")

# --- 4. Añadir elementos ---
# Si la clave no existe, se añade el nuevo par clave-valor.
trabajador["especialidad"] = "Inteligencia artificial"
print(f"Diccionario con añadido: {trabajador}")

# --- 5. Eliminar elementos ---
# Se utiliza la función 'del' indicando la clave.
del trabajador["titulación"]
print(f"Diccionario sin titulación: {trabajador}")

# También se puede usar .pop(), que elimina y DEVUELVE el valor
valor_eliminado = trabajador.pop("especialidad")
print(f"Valor eliminado con .pop(): {valor_eliminado}")
print(f"Diccionario tras .pop(): {trabajador}")

# --- 6. Recorrer elementos (Iteración) ---

# 6.1. Recorrer Claves (Por defecto)
# Utilizando 'for' podemos acceder a las claves y, con ellas, a los valores.
print("\n--- Iterando Claves (default) ---")
for item in trabajador:
    print(f"{item}: {trabajador[item]}") # 'item' es la clave
    # Ejemplo anidado que pedías:
    if item == "conocimientos":
        print(f"\tConocimientos detallados:")
        for c in trabajador[item]: # Itera la lista de conocimientos
            print(f"\t- {c}")

# 6.2. Obtener todas las claves (Método .keys())
print("\n--- Iterando con .keys() ---")
for item in trabajador.keys():
    print(f"Clave: {item}")

# 6.3. Obtener todos los elementos (Método .values())
print("\n--- Iterando con .values() ---")
for item in trabajador.values():
    print(f"Valor: {item}")

# 6.4. Obtener Clave y Valor (Método .items())
# Esta es la forma más común y eficiente para iterar clave y valor juntos.
print("\n--- Iterando con .items() ---")
for key, value in trabajador.items():
    print(f"{key}: {value}")

# --- 7. Otras Operaciones ---

# Copiar (.copy())
my_dict_copy = trabajador.copy()

# Vaciar (.clear())
trabajador.clear()
print(f"\nDiccionario vaciado: {trabajador}")
print(f"Copia intacta: {my_dict_copy}")