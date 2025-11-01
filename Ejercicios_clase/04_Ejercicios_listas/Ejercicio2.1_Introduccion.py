# - INTRODUCCIÓN A PYTHON:

""" Imagina que tienes dos jugadores que introducen sus puntuaciones. El programa
debe:
1. Pedir el nombre y la puntuación de cada jugador.
2. Mostrar operaciones aritméticas entre las puntuaciones (suma, diferencia, etc.).
3. Comparar las puntuaciones y mostrar los resultados (==, >, <, etc.).
4. Mostrar expresiones lógicas compuestas sobre quién tiene más puntos, si son
iguales, etc.
5. Mostrar todos los resultados como parte de un resumen divertido """

# 1. Pedir el nombre y la puntuación de cada jugador.

jugadorNombre1 = input("Introduce el nombre Jugador1:")
jugadorPuntuacion1 = int(input("Introduce la puntuación Jugador1:"))
jugadorNombre2 = input("Introduce el nombre Jugador2:")
jugadorPuntuacion2 = int(input("Introduce la puntuación Jugador2:"))

print("El nombre y puntuación de cada jugador, son:")
print(f"Jugador1: {jugadorNombre1} y {jugadorPuntuacion1}")
print(f"Jugador2: {jugadorNombre2} y {jugadorPuntuacion2}")

# 2. Operaciones aritméticas entre las puntuaciones.

print("\n--- Operaciones Aritméticas ---")

sumaPuntuacion = jugadorPuntuacion1 + jugadorPuntuacion2
print(f"Suma: {jugadorPuntuacion1} + {jugadorPuntuacion2} = {sumaPuntuacion}")

restaPuntuacion = jugadorPuntuacion1 - jugadorPuntuacion2
print(f"Resta: {jugadorPuntuacion1} - {jugadorPuntuacion2} = {restaPuntuacion}")

multiplicacionPuntuacion = jugadorPuntuacion1 * jugadorPuntuacion2
print(f"Multiplicación: {jugadorPuntuacion1} * {jugadorPuntuacion2} = {multiplicacionPuntuacion}")

divisionPuntuacion = jugadorPuntuacion1 / jugadorPuntuacion2
print(f"División (Real): {jugadorPuntuacion1} / {jugadorPuntuacion2} = {divisionPuntuacion}")


print("\n--- Operaciones Adicionales ---")

moduloPuntuacion = jugadorPuntuacion1 % jugadorPuntuacion2
print(f"Módulo (Resto): {jugadorPuntuacion1} % {jugadorPuntuacion2} = {moduloPuntuacion}")

divisionEnteraPuntuacion = jugadorPuntuacion1 // jugadorPuntuacion2
print(f"División Entera: {jugadorPuntuacion1} // {jugadorPuntuacion2} = {divisionEnteraPuntuacion}")

exponentePuntuacion = jugadorPuntuacion1 ** jugadorPuntuacion2
print(f"Exponente: {jugadorPuntuacion1} ** {jugadorPuntuacion2} = {exponentePuntuacion}")

#---------------------------------------------------------------------------------------------------------

# Otra opción 1 y 2:
# Creamos una lista vacía para guardar a los jugadores
jugadores = []

# BUCLE PARA PEDIR DATOS
for i in range(1, 3):
    print(f"--- Datos del Jugador {i} ---")

    nombre = input(f"Introduce el nombre Jugador{i}: ")
    puntuacion = int(input(f"Introduce la puntuación Jugador{i}: "))
    
    # Guardamos los datos (como un diccionario) en la lista
    jugadores.append({
        "nombre": nombre,
        "puntuacion": puntuacion
    })

#  MOSTRAR LOS DATOS INTRODUCIDOS
print("\nEl nombre y puntuación de cada jugador, son:")
print(f"Jugador1: {jugadores[0]['nombre']} y {jugadores[0]['puntuacion']}")
print(f"Jugador2: {jugadores[1]['nombre']} y {jugadores[1]['puntuacion']}")


# BLOQUE DE OPERACIONES
print("\n--- Operaciones (Método Lista/Bucle) ---")

# Accedemos a las puntuaciones desde la lista
p1 = jugadores[0]['puntuacion']
p2 = jugadores[1]['puntuacion']

# Ahora, las operaciones
suma = p1 + p2
print(f"Suma: {p1} + {p2} = {suma}")

resta = p1 - p2
print(f"Resta: {p1} - {p2} = {resta}")

multiplicacion = p1 * p2
print(f"Multiplicación: {p1} * {p2} = {multiplicacion}")

division_real = p1 / p2
print(f"División Real: {p1} / {p2} = {division_real}")

modulo = p1 % p2
print(f"Módulo (Resto): {p1} % {p2} = {modulo}")

division_entera = p1 // p2
print(f"División Entera: {p1} // {p2} = {division_entera}")

exponente = p1 ** p2
print(f"Exponente: {p1} ** {p2} = {exponente}")

#---------------------------------------------------------------------------------------------------------

# 3. Comparar las puntuaciones y mostrar los resultados (==, >, <, etc.).

print("\n--- Comparaciones de Puntuaciones ---")

# Igualdad (==)
print(f"¿Son iguales? ({p1} == {p2}): {p1 == p2}")

# Desigualdad (!=)
print(f"¿Son distintas? ({p1} != {p2}): {p1 != p2}")

# Mayor que (>)
print(f"¿P1 es Mayor? ({p1} > {p2}): {p1 > p2}")

# Menor que (<)
print(f"¿P1 es Menor? ({p1} < {p2}): {p1 < p2}")

# Mayor o Igual que (>=)
print(f"¿P1 es Mayor o Igual? ({p1} >= {p2}): {p1 >= p2}")

# Menor o Igual que (<=)
print(f"¿P1 es Menor o Igual? ({p1} <= {p2}): {p1 <= p2}")

# Comprobar Puntuación 1 (p1)
if p1 % 2 == 0:
    print(f"La puntuación P1 ({p1}) es PAR.")
else:
    print(f"La puntuación P1 ({p1}) es IMPAR.")

# Comprobar Puntuación 2 (p2)
if p2 % 2 == 0:
    print(f"La puntuación P2 ({p2}) es PAR.")
else:
    print(f"La puntuación P2 ({p2}) es IMPAR.")


# 4. Mostrar expresiones lógicas compuestas sobre quién tiene más puntos, si son iguales, etc.

    print("\n--- Expresiones Lógicas Compuestas ---")

# (Usamos 'and', 'or', 'not' para combinar lógicas)

# AND (Ambas deben ser verdad)
print(f"¿Ambas puntuaciones son mayores que 50? ({p1 > 50 and p2 > 50})")

# OR (Al menos una debe ser verdad)
print(f"¿Alguna puntuación es exactamente 0? ({p1 == 0 or p2 == 0})")

# NOT (Invierte el resultado de una comparación)
print(f"¿Es FALSO que p1 ganó? (not {p1 > p2})")

# Combinación (Ej: ¿Ambos son números pares?)
print(f"¿Son ambas puntuaciones pares? ({(p1 % 2 == 0) and (p2 % 2 == 0)})")


# 5. Mostrar todos los resultados como parte de un resumen divertido """

nombre1 = jugadores[0]['nombre']
nombre2 = jugadores[1]['nombre']

print("\n" + "="*30)
print("     RESUMEN DE LA PARTIDA")
print("="*30)

print(f"Jugador 1: {nombre1}, Puntuación: {p1}")
print(f"Jugador 2: {nombre2}, Puntuación: {p2}")

print("\n--- Resultado ---")

if p1 > p2:
    print(f"El ganador es {nombre1}.")
elif p2 > p1:
    print(f"El ganador es {nombre2}.")
else:
    print("El resultado es un empate.")

print(f"La suma total de puntos es: {suma}")

print("\n" + "="*30)
print("        FIN DEL RESUMEN")
print("="*30)