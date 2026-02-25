# Lista global para almacenar los productos (Estructura de datos persistente en ejecución)
inventario = []

def agregar_producto():
    nombre = input("Nombre del producto: ")
    try:
        precio = float(input(f"Precio de '{nombre}': "))
        # Guardamos la información como un diccionario dentro de la lista
        inventario.append({"nombre": nombre, "precio": precio})
        print("Producto agregado con éxito.")
    except ValueError:
        print("Error: El precio debe ser un número.")

def mostrar_productos():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\n--- PRODUCTOS DISPONIBLES ---")
        for p in inventario:
            print(f"- {p['nombre']}: {p['precio']}€")

def buscar_producto():
    nombre_buscar = input("¿Qué producto buscas?: ").lower()
    encontrado = False
    for p in inventario:
        if p['nombre'].lower() == nombre_buscar:
            print(f"El precio de '{p['nombre']}' es {p['precio']}€.")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

def calcular_total():
    # Usamos un acumulador para el precio total
    total = sum(p['precio'] for p in inventario)
    print(f"El valor total del inventario es: {total}€")

def menu():
    while True:
        print("\n--- GESTIÓN DE TIENDA ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Calcular precio total")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            calcular_total()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

# Punto de entrada al programa
if __name__ == "__main__":
    menu()