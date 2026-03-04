### 2.4. Conjuntos (Sets) ###
# Un conjunto (set) es una colección de datos SIN elementos duplicados 
# y NO ordenada (el orden de los elementos no está garantizado).
# Se definen usando llaves {} (si no es vacío) o la función set().

# --- 1. Definición ---

# Creación con set() (para vacíos o desde iterables)
my_set = set() # Crea un conjunto vacío
print(f"Conjunto vacío: {my_set}")

# Creación desde una lista (set() elimina duplicados automáticamente)
numerosSet = set([2, 3, 4, 4, 4]) # Los '4' duplicados se eliminan
print(f"Creado desde lista (duplicados fuera): {numerosSet}")

# Creación con {} (literal)
numeros = {1, 2, 3, 1, 2} # Los duplicados {1, 2} se eliminan automáticamente
print(f"Creado con llaves {1}: {numeros}") # Solo mostrará {1, 2, 3}

print(f"Tipo de dato: {type(numeros)}") # Imprime <class 'set'>


# --- 2. Agregar datos ---
# Se utiliza el método .add().
numeros.add(4)
print(f"Conjunto con .add(4): {numeros}")
numeros.add(2) # Intentar añadir un duplicado (2) no hace nada
print(f"Intentando añadir duplicado (2): {numeros}")


# --- 3. Eliminar datos ---

# .discard(valor): Elimina el elemento SI EXISTE. Si no existe, NO da error.
numeros.discard(1)
print(f"Después de .discard(1): {numeros}")
numeros.discard(99) # Intenta eliminar 99 (no existe), pero no falla
print(f"Después de .discard(99) (no falla): {numeros}")

# .remove(valor): Elimina el elemento. Si NO EXISTE, da 'KeyError'.
numeros.remove(2)
print(f"Después de .remove(2): {numeros}")
# numeros.remove(5) # Daría 'KeyError' porque 5 no está en el conjunto {3, 4}

# .clear(): Vacía todos los datos del conjunto.
numeros.clear()
print(f"Después de .clear(): {numeros}")


# --- 4. Acceso y Recorrido (Iteración) ---

# Nota: Un conjunto NO es ordenado, por lo que NO se puede acceder por índice.
# print(numerosSet[0]) # Daría 'TypeError': 'set' object is not subscriptable

# 4.1. Recorrer los elementos
# Se utiliza una estructura 'for' (el orden de salida no está garantizado).
print("Iterando numerosSet:")
for i in numerosSet:
    print(f"- {i}")

# 4.2. Comprobar pertenencia (Forma de "Acceso")
# La forma de "acceder" es preguntar si un elemento ESTÁ en el conjunto.
print(f"¿Está el 3 en numerosSet?: {3 in numerosSet}") # True
print(f"¿Está el 1 en numerosSet?: {1 in numerosSet}") # False

# 4.3. Conversión para acceso directo
# Si necesitas acceso por índice, debes convertirlo a lista o tupla
my_list_from_set = list(numerosSet)
print(f"Convertido a lista: {my_list_from_set}")
print(f"Acceso al primer ítem de la lista: {my_list_from_set[0]}")


# --- 5. Operaciones de Conjuntos ---
# (Usando los ejemplos del texto)

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}

print(f"\nConjunto 1: {conjunto1}")
print(f"Conjunto 2: {conjunto2}")

# 1. Unión: Valores de ambos, sin duplicados
# (También se puede usar el operador | : conjunto1 | conjunto2)
conjuntoUnion = conjunto1.union(conjunto2)
print(f"Unión (.union): {conjuntoUnion}") # {1, 2, 3, 4, 5, 6, 7}

# 2. Intersección: Valores que están en AMBOS
# (También se puede usar el operador & : conjunto1 & conjunto2)
conjuntoInters = conjunto1.intersection(conjunto2)
print(f"Intersección (.intersection): {conjuntoInters}") # {3, 4, 5}

# 3. Diferencia: Valores que están en el A, pero NO en el B
# (También se puede usar el operador - : conjunto1 - conjunto2)
conjuntoDif = conjunto1.difference(conjunto2)
print(f"Diferencia (.difference) (1-2): {conjuntoDif}") # {1, 2}

# 4. Diferencia Simétrica: Valores que están en A o B, pero NO en ambos
# (También se puede usar el operador ^ : conjunto1 ^ conjunto2)
conjuntoDifSim = conjunto1.symmetric_difference(conjunto2)
print(f"Diferencia Simétrica (.symmetric_difference): {conjuntoDifSim}") # {1, 2, 6, 7}


# --- 6. Eliminación del Set ---
del numerosSet # Elimina la variable 'numerosSet' de la memoria
# print(numerosSet) # Daría 'NameError': name 'numerosSet' is not defined