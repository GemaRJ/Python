from dispositivo import Dispositivo

class Portatil(Dispositivo):
    def __init__(self, marca="", modelo="", version=0, autonomia=0):
        """
        Constructor de Portatil, extiende de Dispositivo y añade autonomía.
        """
        super().__init__(marca, modelo, version)
        self.autonomia = autonomia

    def __str__(self):
        """
        Mostrar datos incluyendo autonomía.
        """
        base_str = super().__str__()
        return f"{base_str}, Autonomía: {self.autonomia} horas"

    def actualizar_firmware(self):
        """
        Sobrescribe el método para actualizar BIOS y controladores.
        """
        print(f"Actualizando BIOS y controladores de {self.marca} {self.modelo}...")
        self.version += 1
        print(f"Versión actualizada a {self.version}\n")