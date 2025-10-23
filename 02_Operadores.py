### Operadores Aritméticos ###

# Operaciones con enteros:

print(3 + 4)     # Suma: 7
print(3 - 4)     # Resta: -1
print(3 * 4)     # Multiplicación: 12
print(3 / 4)     # División (siempre devuelve float): 0.75
print(10 % 3)    # Módulo (resto de la división): 1
print(10 // 3)   # División de suelo (descarta decimales): 3
print(2 ** 3)    # Exponente (2 elevado a 3): 8
print(2 ** 3 + 3 - 7 / 1 // 4) # Combinación: 8 + 3 - (7.0 // 4.0) = 11.0 - 1.0 = 10.0

#-------------------------------------------------------------------------------------------------------

# Operaciones con cadenas de texto:

print("Hola " + "Python " + "¿Qué tal?") # Concatenación (unión) de strings: "Hola Python ¿Qué tal?"
print("Hola " + str(5))                 # Concatena un string con un int convertido a string: "Hola 5"

#-------------------------------------------------------------------------------------------------------

# Operaciones mixtas:

print("Hola " * 5)                      # Repite el string 5 veces: "Hola Hola Hola Hola Hola "
print("Hola " * (2 ** 3))               # Repite el string 8 veces (primero calcula 2**3): "Hola Hola ... (8 veces)"

my_float = 2.5 * 2                      # my_float vale 5.0 (tipo float)
print("Hola " * int(my_float))          # Convierte el float 5.0 a int 5 y repite el string 5 veces.

#-------------------------------------------------------------------------------------------------------

### Operadores Comparativos ###

# Operaciones con enteros:

print(3 > 4)    # Mayor que: False
print(3 < 4)    # Menor que: True
print(3 >= 4)   # Mayor o igual que: False
print(4 <= 4)   # Menor o igual que: True
print(3 == 4)   # Igual que: False
print(3 != 4)   # Distinto que: True

# Operaciones con cadenas de texto (compara por orden alfabético/ASCII):

print("Hola" > "Python")  # Compara "H" vs "P". "H" va antes, así que: False
print("Hola" < "Python")  # Compara "H" vs "P". "H" va antes, así que: True
print("aaaa" >= "abaa")   # Compara "a" vs "b" en el segundo carácter: False
print(len("aaaa") >= len("abaa")) # Compara la longitud (4 >= 4): True
print("Hola" <= "Python") # Compara "H" vs "P": True
print("Hola" == "Hola")   # Igual que: True
print("Hola" != "Python") # Distinto que: True

#-------------------------------------------------------------------------------------------------------

### Operadores Lógicos ###

# Basada en el Álgebra de Boole (and, or, not):

print(3 > 4 and "Hola" > "Python")     # False and False: False
print(3 > 4 or "Hola" > "Python")      # False or False: False
print(3 < 4 and "Hola" < "Python")     # True and True: True
print(3 < 4 or "Hola" > "Python")      # True or False: True
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # True or (False and True) -> True or False: True
print(not (3 > 4))                     # not (False): True