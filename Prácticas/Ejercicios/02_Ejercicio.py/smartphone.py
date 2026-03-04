from dispositivo import Dispositivo

class Smartphone(Dispositivo):
    def __init__(self, marca="", modelo="", version=0, camaras=0):
        """
        Constructor de Smartphone, extiende de Dispositivo y añade cámaras.
        """
        super().__init__(marca, modelo, version)
        self.camaras = camaras

    def __str__(self):
        """
        Mostrar datos incluyendo cámaras.
        """
        base_str = super().__str__()
        return f"{base_str}, Cámaras: {self.camaras}"

    def actualizar_firmware(self):
        """
        Sobrescribe el método para actualizar sistema operativo Android/iOS.
        """
        print(f"Actualizando sistema operativo Android/iOS de {self.marca} {self.modelo}...")
        self.version += 1
        print(f"Versión actualizada a {self.version}\n")