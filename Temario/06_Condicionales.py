# IF

my_condition = False # Asignamos el valor Booleano False a la variable

if my_condition:                            # Comprueba si my_condition es True (lo es por defecto si no es False, 0, None o vacío)
    print("Se ejecuta la condición del if") # Esta línea NO se ejecuta porque my_condition es False

my_condition = 5 * 5 # Sobrescribimos my_condition con el resultado de 5*5, que es 25 (un int)

if my_condition == 10: # Comprueba si el valor de my_condition es 10 (25 == 10 es False)
    print("Se ejecuta la condición del segundo if") # Esta línea NO se ejecuta

# IF, ELIF, ELSE

# Empieza una nueva estructura condicional. my_condition sigue valiendo 25.

if my_condition > 10 and my_condition < 20: # Comprueba (25 > 10 and 25 < 20) -> (True and False) -> False
    print("Es mayor que 10 y menor que 20") # NO se ejecuta
elif my_condition == 25:                    # Como el 'if' falló, comprueba esta: (25 == 25) -> True
    print("Es igual a 25")                  # SÍ se ejecuta esta línea
else:                                       # Como el 'elif' fue True, esta parte se ignora y no se ejecuta
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")              # Esta línea se ejecuta siempre, al estar fuera del if/elif/else



# ESTRUCTURA MATCH:

# Pide al usuario que escriba algo y lo guarda en la variable 'opcion' (como string)
opcion = input("Selecciona una opción (1, 2, 3):") 

match opcion:                                          # Inicia una comprobación 'match-case' (similar a switch) sobre el valor de 'opcion'
 case "1":                                             # Comprueba si el valor de 'opcion' es exactamente el string "1"
  print("Has seleccionado la opción 1: Ver perfil.")   # Se ejecuta si el caso es "1"
 case "2":                                             # Si no fue "1", comprueba si es el string "2"
  print("Has seleccionado la opción 2: Editar perfil.")# Se ejecuta si el caso es "2"
 case "3":                                             # Si no fue "1" ni "2", comprueba si es el string "3"
  print("Has seleccionado la opción 3: Cerrar sesión.")# Se ejecuta si el caso es "3"
 case _:                        # Este es el 'caso por defecto' (wildcard). Se ejecuta si ninguno de los anteriores coincide.
  print("Opción no válida. Inténtalo de nuevo.") # Se ejecuta si la 'opcion' no fue "1", "2" ni "3".

# Condicional con inspección de valor

my_string = "" # Asignamos una cadena de texto vacía a la variable

if not my_string: # 'not' invierte el valor Booleano. Un string vacío se evalúa como False. 'not False' es True.
    print("Mi cadena de texto es vacía") # SÍ se ejecuta

if my_string == "Mi cadena de textoooooo": # Comprueba si "" es igual a "...", lo cual es False
    print("Estas cadenas de texto coinciden") # NO se ejecuta