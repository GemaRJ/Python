# Gestión de Inventario de una Tienda.
# Este programa permite gestionar el inventario de una tienda. Permite cargar datos desde un archivo,
# mostrar el inventario, calcular el valor total, mostrar productos agotados y actualizar cantidades.   

import os

ARCHIVO = "inventario.txt"

# Función para cargar el inventario desde el archivo.
def cargar_inventario():
    inventario = {}

    # Si el archivo no existe o está vacío, se crea con un inventario inicial.
    if not os.path.exists(ARCHIVO) or os.stat(ARCHIVO).st_size == 0:
        print("No existe inventario.txt o está vacío. Creamos un inventario nuevo.")
        inventario_inicial = {
            "Portátil": [800, 10],
            "Teléfono": [1300, 1],
            "Tablet": [200.00, 8],
            "Auriculares": [50.99, 0]
        }
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            for nombre, datos in inventario_inicial.items():
                f.write(f"{nombre},{datos[0]},{datos[1]}\n")
        return inventario_inicial

    # Si el archivo existe y tiene datos, se lee.
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                try:
                    nombre, precio, cantidad = linea.split(",")
                    inventario[nombre] = [float(precio), int(cantidad)]
                except ValueError:
                    print(f"Error al leer la línea: {linea}")
    return inventario


# Función para mostrar el inventario.
def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n=== INVENTARIO DE LA TIENDA ===")
    print(f"{'Producto':<15}{'Precio (€)':<12}{'Cantidad':<10}")
    print("-" * 37)
    for nombre, datos in inventario.items():
        print(f"{nombre:<15}{datos[0]:<12.2f}{datos[1]:<10}")
    print("-" * 37)


# Función para calcular el valor total del inventario.
def calcular_valor_total(inventario):
    total = sum(precio * cantidad for precio, cantidad in inventario.values())
    print(f"\nValor total del inventario: {total:.2f} €")


# Función para mostrar los productos agotados.
def mostrar_agotados(inventario):
    agotados = [nombre for nombre, datos in inventario.items() if datos[1] == 0]
    if agotados:
        print("\nProductos agotados:")
        for p in agotados:
            print(f" - {p}")
    else:
        print("\nNo hay productos agotados.")


# Función para actualizar la cantidad de un producto.
def actualizar_producto(inventario):
    nombre = input("Introduce el nombre del producto que deseas actualizar: ")

    if nombre not in inventario:
        print("El producto no existe en el inventario.")
        return inventario

    try:
        nueva_cantidad = int(input("Nueva cantidad: "))
        inventario[nombre][1] = nueva_cantidad
        guardar_inventario(inventario)
        print(f"Cantidad de '{nombre}' actualizada correctamente.")
    except ValueError:
        print("La cantidad debe ser un número entero.")
    return inventario


# Función para guardar los datos en el archivo.
def guardar_inventario(inventario):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for nombre, datos in inventario.items():
            f.write(f"{nombre},{datos[0]},{datos[1]}\n")


# Función principal con el menú-interfaz.
def menu():
    inventario = cargar_inventario()

    while True:
        print("\n=== MENÚ DE GESTIÓN DE INVENTARIO ===")
        print("1. Mostrar inventario")
        print("2. Calcular valor total del inventario")
        print("3. Mostrar productos agotados")
        print("4. Actualizar cantidad de un producto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            calcular_valor_total(inventario)
        elif opcion == "3":
            mostrar_agotados(inventario)
        elif opcion == "4":
            inventario = actualizar_producto(inventario)
        elif opcion == "5":
            print("Saliendo del programa del inventario...")
            break
        else:
            print("Opción no válida, introduce una opción correcta.")


# Ejecución del programa
if __name__ == "__main__":
    menu()
