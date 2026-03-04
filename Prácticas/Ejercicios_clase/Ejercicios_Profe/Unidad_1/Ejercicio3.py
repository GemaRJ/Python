""" 
El programa deberá cumplir los siguientes requisitos funcionales:
1. Mostrar un mensaje de bienvenida al iniciar la aplicación.
2. Permitir introducir varios productos, cada uno con:
- Nombre del producto (cadena de texto)
- Cantidad en stock (entero)
- Precio por unidad (número decimal)
3. Usar un bucle while que permita seguir introduciendo productos hasta que el usuario deje el campo del
nombre vacío.
4. Validar que la cantidad y el precio sean valores numéricos (controlar errores con try-except).
5. Guardar los productos en una lista de diccionarios, por ejemplo:
6. [
7. {"nombre": "Ratón", "cantidad": 15, "precio": 12.5},
8. {"nombre": "Teclado", "cantidad": 10, "precio": 25.0}
9. ]
10. Al finalizar la entrada de datos, recorrer la lista con un bucle for y:
o Calcular el valor total de cada producto (cantidad * precio)
o Mostrar cada producto en formato:
o Ratón: 15 unidades x 12.5 € = 187.50 €
11. Calcular el valor total del inventario sumando el valor de todos los productos.
12. Mostrar al final un mensaje con el valor total y una despedida.

 """

print("¡Bienvenido al gestor de inventario!")

productos = []

while True:
    nombre = input("Introduce el nombre del producto (deja vacío para terminar): ")
    if nombre == "":
        break

    # Crear un diccionario nuevo para cada producto
    producto = {
        "nombre": nombre,
        "cantidad": 0,
        "precio": 0.0
    }

    while True:
        try:
            cantidad = int(input("Introduce la cantidad en stock: "))
            producto["cantidad"] = cantidad
            break
        except ValueError:
            print("Por favor, introduce un número entero válido para la cantidad.")

    while True:
        try:
            precio = float(input("Introduce el precio por unidad: "))
            producto["precio"] = precio
            break
        except ValueError:
            print("Por favor, introduce un número decimal válido para el precio.")

    productos.append(producto)

print("\n=== LISTADO DE INVENTARIO ===")

valor_total = 0

for producto in productos:
    valor = producto["cantidad"] * producto["precio"]
    print(f"{producto['nombre']}: {producto['cantidad']} unidades x {producto['precio']}€ = {valor:.2f}€")
    valor_total += valor

print(f"\nValor total del inventario: {valor_total:.2f}€")
print("--- Fin del programa ---")
