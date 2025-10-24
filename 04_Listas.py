### 2.1. Listas ###

""" --- 1. Definición ---
# Estructura de datos ordenadas. Sus datos están asociadas a posiciones. Siendo la primera posición el 0.
Para poderla crear, se utiliza []
"""
# Crear listas vacías
my_list = list() # Crea una lista vacía usando el constructor list()
my_other_list = [] # Crea una lista vacía usando la sintaxis literal (preferida)

print(my_list) # Imprime la lista vacía: []
print(len(my_list)) # Imprime la longitud de la lista vacía (0)

# Crear listas con valores iniciales
my_list = [35, 24, 62, 52, 30, 30, 17] # Reasigna 'my_list' con valores iniciales
print(my_list) # Imprime el contenido de la lista
print(len(my_list)) # Imprime la longitud de la lista (7) (¡Este era el error, ya está corregido!)

# Las listas pueden mezclar tipos de datos
my_other_list = [35, 1.77, "Gema", "Rodriguez"] 

print(type(my_list)) # Imprime el tipo de 'my_list' (<class 'list'>)
print(type(my_other_list)) # Imprime el tipo de 'my_other_list' (<class 'list'>)

# --- 2. Acceso a elementos y búsqueda ---

# Acceso por índice (empieza en 0)
print(my_other_list[0]) # Accede al primer elemento (índice 0): 35
print(my_other_list[1]) # Accede al segundo elemento (índice 1): 1.77
print(my_other_list[-1]) # Accede al último elemento (índice -1): "Rodriguez"
print(my_other_list[-4]) # Accede al primer elemento (índice -4 en esta lista): 35
# print(my_other_list[4]) # Daría error IndexError: fuera de rango
# print(my_other_list[-5]) # Daría error IndexError: fuera de rango

# Búsqueda
print(my_list.count(30)) # Cuenta cuántas veces aparece el valor 30 en 'my_list': 2
print(my_other_list.index("Gema")) # Devuelve el índice del primer elemento que coincida: 2

# Desempaquetado (asignar elementos a variables)
age, height, name, surname = my_other_list 
print(name) # Imprime la variable 'name' ("Gema")

# Asignación manual de variables
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age) # Imprime la variable 'age' (35)


# --- 3. Modificar un dato ---
# Se accede por el índice y se reasigna el valor
my_other_list[1] = "Azul" # Actualiza (reemplaza) el valor en el índice 1
print(my_other_list)


# --- 4. Agregar elementos ---
my_other_list.append("Rodríguez") # Añade un elemento al FINAL de la lista
print(my_other_list)

my_other_list.insert(1, "Rojo") # Inserta "Rojo" en el índice 1 (desplazando el resto)
print(my_other_list)


# --- 5. Eliminar elementos ---
my_other_list.remove("Azul") # Elimina la PRIMERA aparición del valor "Azul"
print(my_other_list)

my_list.remove(30) # Elimina la PRIMERA aparición del valor 30
print(my_list) # (Nota: el segundo 30 sigue en la lista)

# .pop() elimina y DEVUELVE el elemento (por defecto el último)
print(my_list.pop()) # Elimina Y DEVUELVE el ÚLTIMO elemento de la lista (17)
print(my_list) # Muestra la lista sin el último elemento

# .pop(indice) elimina y DEVUELVE el elemento de ese índice
my_pop_element = my_list.pop(2) # Elimina Y DEVUELVE el elemento en el índice 2 (62)
print(my_pop_element) # Imprime el elemento eliminado (62)
print(my_list) # Muestra la lista sin ese elemento

# 'del' elimina por índice
del my_list[2] # Elimina el elemento en el índice 2 (ahora es 52) usando 'del'
print(my_list)


# --- 6. Operaciones con listas ---

# Concatenación
print(my_list + my_other_list) # Suma (concatena) dos listas, creando una nueva lista
#print(my_list - my_other_list) # Restar listas no está permitido (daría TypeError)

# Copiar
my_new_list = my_list.copy() # Crea una copia superficial de la lista

# Vaciar
my_list.clear() # Vacía la lista original (elimina todos sus elementos)
print(my_list) # Imprime la lista vacía: []
print(my_new_list) # La copia ('my_new_list') permanece intacta

# Ordenar y Revertir (se hacen "in-place", modifican la lista original)
my_new_list.reverse() # Invierte el orden de los elementos
print(my_new_list)

my_new_list.sort() # Ordena los elementos de menor a mayor
print(my_new_list)

# Sublistas (Slicing)
# Crea una nueva lista desde el índice 1 (incluido) hasta el 3 (excluido)
print(my_new_list[1:3]) 


# --- 7. Cambio de tipo ---
# Una variable puede cambiar de tipo si se le reasigna
my_list = "Hola Python" # La variable 'my_list' ahora apunta a un string
print(my_list) # Imprime el string
print(type(my_list)) # Imprime el nuevo tipo: <class 'str'>