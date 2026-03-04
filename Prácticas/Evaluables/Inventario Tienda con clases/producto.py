class Producto:
     #  Representa un producto de la tienda con nombre, precio y cantidad.
    def __init__(self, nombre, precio, cantidad):
        # Constructor de la clase Producto.  
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def __str__(self):
    # Define cómo se debe imprimir un objeto Producto. Ej: "Portatil|799.99 € | 10
        return f"{self.nombre:<15} | {self.precio:>12.2f} € | {self.cantidad:>10}"