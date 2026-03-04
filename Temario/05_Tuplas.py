### 2.2. Tuplas ###
# Las tuplas son estructuras de datos ordenadas, igual que las listas,
# pero con la diferencia clave de que son INMUTABLES.
# No se pueden modificar, agregar o eliminar elementos después de su creación.
# Se definen usando paréntesis ().

# --- 1. Definición ---
my_tuple = tuple() # Crea una tupla vacía usando el constructor
my_other_tuple = () # Crea una tupla vacía usando la sintaxis literal

# Inicialización con datos
my_tuple = (35, 1.77, "GEMA", "RODRIGUEZ", "GEMA")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple)) # Imprime <class 'tuple'>


# --- 2. Acceso a elementos y búsqueda ---

# Acceso por índice (igual que las listas)
print(my_tuple[0]) # Accede al primer elemento (35)
print(my_tuple[-1]) # Accede al último elemento ("GEMA")
# print(my_tuple[5]) # Daría error IndexError: fuera de rango
# print(my_tuple[-6]) # Daría error IndexError: fuera de rango

# Búsqueda
print(my_tuple.count("GEMA")) # Cuenta cuántas veces aparece "GEMA" (2)
print(my_tuple.index("RODRIGUEZ")) # Devuelve el índice de "RODRIGUEZ" (3)
# print(my_tuple.index("Jorge")) # Daría error 'ValueError' porque "Jorge" no está en la tupla.

# Subtuplas (Slicing)
# (Esto crea una tupla NUEVA, no modifica la original)
my_sum_tuple = my_tuple + my_other_tuple # (Necesitamos la tupla suma para este ejemplo)
print(my_sum_tuple[3:6]) # Muestra desde el índice 3 hasta el 6 (sin incluir el 6)


# --- 3. Operaciones con Tuplas ---

# Concatenación (Crea una NUEVA tupla)
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)


# --- 4. El "truco" para modificar (Conversión) ---
# Para "modificar" una tupla, el truco es convertirla a lista,
# modificar la lista, y volver a convertirla en tupla.

my_tuple = list(my_tuple) # 1. Convertir a lista
print(type(my_tuple)) # Imprime <class 'list'>

my_tuple[4] = "Rodríguez" # 2. Modificar la lista (antes "GEMA")
my_tuple.insert(1, "Azul") # 3. Insertar en la lista
print(my_tuple) # Muestra la lista modificada

my_tuple = tuple(my_tuple) # 4. Volver a convertir a tupla
print(my_tuple) # Muestra la nueva tupla
print(type(my_tuple)) # Imprime <class 'tuple'>


# --- 5. Eliminación de la Tupla ---
# No puedes borrar un elemento (del my_tuple[2]), pero sí la variable entera.
