# FOR

my_list = [35, 24, 62, 52, 30, 30, 17] # Define una lista

for element in my_list: # Bucle 'For': recorre cada elemento en 'my_list'
    print(element) # Imprime el elemento actual de la lista

my_tuple = (35, 1.77, "Gema", "Rodríguez", "Jorge") # Define una tupla

for element in my_tuple: # Recorre cada elemento en 'my_tuple'
    print(element) # Imprime el elemento actual de la tupla

my_set = {"Gema", "Rodríguez", 35} # Define un set (conjunto, orden no garantizado)

for element in my_set: # Recorre cada elemento en 'my_set'
    print(element) # Imprime el elemento actual (el orden puede variar)

my_dict = {"Nombre": "Gema", "Apellido": "Rodríguez", "Edad": 37, 1: "Python"} # Define un diccionario

for element in my_dict: # Por defecto, un 'for' sobre un diccionario recorre sus CLAVES
    print(element) # Imprime la clave actual ("Nombre", "Apellido", "Edad"...)
    if element == "Edad": # Comprueba si la clave es "Edad"
        break # Si es "Edad", rompe el bucle (no seguirá a la clave 1)
else: # El 'else' de un 'for' se ejecuta si el bucle termina naturalm_ente (SIN 'break')
    print("El bucle for para el diccionario ha finalizado") # Esta línea NO se ejecutará por el 'break'

print("La ejecución continúa") # Se ejecuta después de que el bucle se rompiera

for element in my_dict: # Vuelve a recorrer las CLAVES del diccionario
    print(element) # Imprime la clave actual
    if element == "Edad": # Comprueba si la clave es "Edad"
        continue # Si es "Edad", salta al siguiente elemento (ignora el resto del código de esta iteración)
    print("Se ejecuta") # Se imprime para "Nombre", "Apellido" y 1, pero NO para "Edad"
else: # Se ejecuta porque este bucle SÍ termina de forma natural (no hubo 'break')
    print("El bluce for para diccionario ha finalizado") # (sic) Se ejecuta al finalizar el bucle


# WHILE

my_condition = 0 # Inicializa la variable 'my_condition' en 0

while my_condition < 10: # Bucle: se ejecuta mientras 'my_condition' sea menor que 10
    print(my_condition) # Imprime el valor actual de 'my_condition' (0, 2, 4, 6, 8)
    my_condition += 2 # Incrementa 'my_condition' en 2 en cada iteración
else:  # Es opcional. Se ejecuta SOLO cuando el bucle termina de forma natural (sin 'break')
    print("Mi condición es mayor o igual que 10") # Se ejecuta cuando 'my_condition' llega a 10

print("La ejecución continúa") # Se ejecuta después de que el bucle (y su 'else') termine

# (Ahora 'my_condition' vale 10)
while my_condition < 20: # Bucle: se ejecuta mientras 'my_condition' (que vale 10) sea menor que 20
    my_condition += 1 # Incrementa en 1 (el primer valor en comprobar será 11)
    if my_condition == 15: # Comprueba si el valor ha llegado a 15
        print("Se detiene la ejecución") # Imprime este mensaje
        break # Interrumpe (rompe) el bucle 'while' inmediatamente
    print(my_condition) # Imprime el valor (imprimirá de 11 a 14)

print("La ejecución continúa") # Se ejecuta después de que el bucle se rompiera con 'break'
