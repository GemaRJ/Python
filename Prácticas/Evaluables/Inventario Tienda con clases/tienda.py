from gestion_inventario import GestionInventario

class Tienda:
    #    Clase principal que maneja el menú y la interacción con el usuario
    def __init__(self):
        #Constructor de Tienda. Crea una instancia del gestor.
     
        # Creamos una instancia del gestor de inventario
        self.gestor = GestionInventario()

    def mostrar_menu(self):
    # Imprime el menú de opciones.
        
        print("\n--- MENÚ GESTIÓN DE TIENDA ---")
        print("1. Mostrar inventario")
        print("2. Actualizar cantidad de un producto")
        print("3. Mostrar productos agotados")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

    def ejecutar(self):
       # Inicia el bucle principal del programa.
  
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción (1-5): ").strip()

            if opcion == '1':
                # Llama al método de la otra clase
                self.gestor.mostrar_inventario()

            elif opcion == '2':
                print("\n---  ACTUALIZAR CANTIDAD ---")
                
                # --- ESTA ES LA LÍNEA CORREGIDA ---
                # .strip() quita espacios.
                # .title() convierte "portatil" o "PORTATIL" en "Portatil".
                nombre = input("Nombre del producto a actualizar: ").strip().title()
                
                try:
                    cantidad = int(input(f"Introduce la nueva cantidad para '{nombre}': "))
                    # Llama al método de la otra clase con los datos
                    self.gestor.actualizar_cantidad(nombre, cantidad)
                except ValueError:
                    print(" Error: La cantidad debe ser un número entero.\n")

            elif opcion == '3':
                self.gestor.identificar_agotados()

            elif opcion == '4':
                self.gestor.calcular_valor_total()

            elif opcion == '5':
                print("\nSaliendo del programa. ¡Hasta pronto!")
                break # Termina el bucle while

            else:
                print(" Opción no válida. Introduce un número del 1 al 5.\n")

# --- Punto de entrada del script ---
# Esto asegura que el código solo se ejecuta si corres este archivo
if __name__ == "__main__":
    # 1. Creamos un objeto Tienda
    mi_tienda = Tienda()
    # 2. Ejecutamos su método principal (que contiene el bucle)
    mi_tienda.ejecutar()