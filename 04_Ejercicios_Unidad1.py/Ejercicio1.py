""" ENUNCIADO: 

Se desea realizar un programa que trabaje con tres números enteros introducidos por el usuario.
El programa debe:
1. Solicitar al usuario tres números enteros (num1, num2, num3).
2. Mostrar los números introducidos, indicando su tipo de dato (int).
3. Calcular y mostrar:
o El mayor y el menor.
o La suma de los tres números.
o La resta secuencial (num1 - num2 - num3).
o El producto (num1 * num2 * num3).
o El cociente real de dividir la suma entre 3 (/).
o La división entera (//) de la suma entre 3.
o El resto (%) de la suma entre 3.
o La potencia del mayor elevado al menor.
4. Convertir la media aritmética a entero (con int) y mostrarla.
5. Convertir la suma a cadena de texto y mostrar el mensaje: "La suma como texto es: <valor>".
6. Indicar si la suma es par o impar.
7. Mostrar si la media real es mayor, menor o igual a 10.

"""

#1. Solicitar al usuario tres números enteros (num1, num2, num3).
#2. Mostrar los números introducidos, indicando su tipo de dato (int).

print("--- EJERCICIO PROFESOR UNIDAD-1 ---")

# Usamos int() para convertir la entrada (str) a entero (int)
num1 = int(input("Introduce el primero número:"))
num2 = int(input("Introduce el segundo número:"))
num3 = int(input("Introduce el tercer número:"))


print(f"Los números elegidos por el usuario, son: {num1}, {num2} y {num3}")
print(f"El tipo de dato de num1 es: {type(num1)}")


# 3. Calcular y mostrar:
# El mayor y el menor.

numMayor = max(num1, num2, num3)
numMenor = min(num1, num2, num3)

print(f"El número MAYOR de los tres es: {numMayor}")
print(f"El número MENOR de los tres es: {numMenor}")


# La suma de los tres números.

numSuma=num1+num2+num3
numResultado=numSuma
print(f"La suma de los tres números elegidos, es:{numResultado} ")

# Otra opción más directa:

# La suma de los tres números.

numSuma = num1 + num2 + num3
print(f"La suma de los tres números elegidos, es: {numSuma}")

# La resta secuencial (num1 - num2 - num3).

numResta = num1 - num2 - num3
print(f"La resta de los tres números elegidos, es: {numResta}")

# El producto (num1 * num2 * num3).

numMultiplicacion = num1 * num2 * num3
print(f"La multiplicación de los tres números elegidos, es: {numMultiplicacion}")

# La división entera (//) de la suma entre 3.

numDivisionEntera = numSuma // 3

print(f"La división entera de la suma ({numSuma}) entre 3, es: {numDivisionEntera}")