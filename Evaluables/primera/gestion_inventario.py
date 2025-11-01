import os
from producto import Producto

class GestionInventario:
  # Maneja todas las operaciones lógicas del inventario: Cargar, guardar, actualizar, y realizar cálculos.
   
    def __init__(self, nombre_archivo="inventario.txt"):
        # Constructor de la clase.
        
        self.archivo = nombre_archivo
        # El inventario será un diccionario de objetos Producto
        # Ejemplo: {"Portatil": Producto("Portatil", 799.99, 10)}
        self.inventario = {}
        # Cargamos los datos al iniciar
        self.cargar_inventario()

    def _crear_archivo_default(self):
       # Método privado para crear un inventario.txt con datos iniciales.

        print(f"Advertencia: No se encontró '{self.archivo}'.")
        print("Creando archivo con inventario inicial...")
        try:
            default_items = [
                Producto("Portatil", 799.99, 10),
                Producto("Telefono", 299.99, 25),
                Producto("Tablet", 199.50, 15),
                Producto("Smartwatch", 149.00, 0)
            ]
            # Guardamos los items por defecto en el diccionario
            for item in default_items:
                self.inventario[item.nombre] = item
            
            # Y ahora guardamos en el archivo físico
            self.guardar_inventario()
            
        except IOError as e:
            print(f"No se pudo crear el archivo '{self.archivo}': {e}")

    def cargar_inventario(self):
        # (Requisito 1) Carga los productos desde el archivo de texto. Si el archivo no existe, llama a _crear_archivo_default().

        if not os.path.exists(self.archivo):
            self._crear_archivo_default()
            return # Ya tenemos el inventario cargado

        # Si sí existe, lo leemos
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        try:
                            nombre, precio, cantidad = linea.split(",")
                            # Creamos un objeto Producto y lo guardamos
                            self.inventario[nombre] = Producto(nombre, precio, cantidad)
                        except ValueError:
                            print(f" Línea inválida en el archivo: {linea}. Se omitirá.")
            print(" Inventario cargado correctamente.\n")
        except IOError as e:
            print(f" Error al leer el archivo '{self.archivo}': {e}")

    def guardar_inventario(self):
        #(Requisito 5 - parte de actualizar) Guarda el inventario actual de vuelta en el archivo.
      
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for producto in self.inventario.values():
                    f.write(f"{producto.nombre},{producto.precio},{producto.cantidad}\n")
        except IOError as e:
            print(f"No se pudo guardar en '{self.archivo}': {e}")

    def mostrar_inventario(self):
       #(Requisito 2) Muestra en pantalla los productos en formato claro.
      
        print("\n--- INVENTARIO ACTUAL ---")
        print("=================================================")
        print(f"{'Producto':<15} | {'Precio (EUR)':>12} | {'Cantidad':>10}")
        print("-------------------------------------------------")
        if not self.inventario:
            print("El inventario está vacío.")
        else:
            for producto in self.inventario.values():
                print(producto) # Usa el método __str__ de la clase Producto
        print("=================================================\n")

    def calcular_valor_total(self):
     #(Requisito 3) Calcula y devuelve el valor total del inventario.
   
        total = 0.0
        for producto in self.inventario.values():
            total += producto.precio * producto.cantidad
        
        print(f"💰 Valor total del inventario: {total:.2f} €\n")

    def identificar_agotados(self):
        # (Requisito 4) Identifica y muestra productos con stock 0.
     
        print("\n---  PRODUCTOS AGOTADOS ---")
        agotados = []
        for producto in self.inventario.values():
            if producto.cantidad == 0:
                agotados.append(producto.nombre)
        
        if not agotados:
            print(" No hay productos agotados.\n")
        else:
            for nombre in agotados:
                print(f"- {nombre}")
            print() # Salto de línea

    def actualizar_cantidad(self, nombre_producto, nueva_cantidad):
        #(Requisito 5) Permite modificar la cantidad de un producto.
  
        if nombre_producto not in self.inventario:
            print(f" Error: El producto '{nombre_producto}' no existe.\n")
            return

        if nueva_cantidad < 0:
            print(" Error: La cantidad no puede ser negativa.\n")
            return
            
        # Actualizamos la cantidad en el objeto Producto
        self.inventario[nombre_producto].cantidad = nueva_cantidad
        
        # Guardamos todos los cambios en el archivo
        self.guardar_inventario()
        print(f" Cantidad de '{nombre_producto}' actualizada a {nueva_cantidad}.\n")