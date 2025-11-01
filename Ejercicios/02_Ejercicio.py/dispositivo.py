class Dispositivo:
    def __init__(self, marca="", modelo="", version=0):
        """
        Constructor vacío o con parámetros para inicializar un dispositivo.
        """
        self.marca = marca
        self.modelo = modelo
        self.version = version

    def __str__(self):
        """
        Método para mostrar todos los datos del dispositivo.
        """
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Versión: {self.version}"

    def actualizar_firmware(self):
        """
        Simula la actualización del firmware incrementando la versión en 1.
        """
        print(f"Actualizando firmware de {self.marca} {self.modelo}...")
        self.version += 1
        print(f"Versión actualizada a {self.version}\n")