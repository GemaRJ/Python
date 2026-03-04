# --- PROGRAMA DE GESTIÓN DE TIENDA ---

# Lista global para almacenar los productos
inventario = []

def agregar_producto():
    """Registra un producto con nombre y precio."""
    nombre = input("Nombre del producto: ")
    try:
        precio = float(input(f"Precio de '{nombre}': "))
        # Guardamos como diccionario para organizar la información
        inventario.append({"nombre": nombre, "precio": precio})
        print(f"Producto '{nombre}' agregado con éxito.")
    except ValueError:
        print("Error: El precio debe ser un número decimal (ej: 10.5).")

def mostrar_productos():
    """Muestra todos los productos en el inventario."""
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\n--- INVENTARIO DISPONIBLE ---")
        for p in inventario:
            print(f"Producto: {p['nombre']} | Precio: {p['precio']}€")

def buscar_producto():
    """Busca un producto por nombre y muestra su precio."""
    busqueda = input("Introduce el nombre del producto a buscar: ").lower()
    encontrado = False
    for p in inventario:
        if p['nombre'].lower() == busqueda:
            print(f"Resultado: {p['nombre']} cuesta {p['precio']}€.")
            encontrado = True
            break
    if not encontrado:
        print("Lo sentimos, el producto no existe en la tienda.")

def calcular_total():
    """Suma el precio de todos los productos del inventario."""
    # Usamos una expresión generadora para sumar los precios
    total = sum(p['precio'] for p in inventario)
    print(f"El valor total de todos los productos es: {total}€")

def menu():
    """Gestiona el flujo principal y el menú de usuario (RA 2: Estructuras de control)."""
    while True:
        print("\n=== MENÚ DE LA TIENDA ===")
        print("1. Agregar producto")
        print("2. Mostrar todos los productos")
        print("3. Buscar producto por nombre")
        print("4. Calcular precio total")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            calcular_total()
        elif opcion == "5":
            print("Cerrando el sistema... ¡Buen día!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu()