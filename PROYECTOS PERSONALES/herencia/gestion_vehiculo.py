# PROGRAMA: gestion_vehiculos.py
# DESCRIPCIÓN:
# Programa de gestión de vehículos de una empresa de transporte
# usando Programación Orientada a Objetos.
# En este ejercicio se aplican:
# - Encapsulación
# - Herencia
# - Polimorfismo
# - Abstracción

from abc import ABC, abstractmethod


# CLASE BASE ABSTRACTA: Vehiculo
class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        # Atributos privados
        self.__marca = marca
        self.__modelo = modelo

    # Getter de marca
    def get_marca(self):
        return self.__marca

    # Setter de marca
    def set_marca(self, marca):
        self.__marca = marca

    # Getter de modelo
    def get_modelo(self):
        return self.__modelo

    # Setter de modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo

    # Método común
    def mostrar_info(self):
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")

    # Método abstracto
    @abstractmethod
    def calcular_coste(self):
        pass


# CLASE HIJA: Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.__num_puertas = num_puertas

    # Getter
    def get_num_puertas(self):
        return self.__num_puertas

    # Setter
    def set_num_puertas(self, num_puertas):
        self.__num_puertas = num_puertas

    # Polimorfismo
    def mostrar_info(self):
        print("=== COCHE ===")
        print(f"Marca: {self.get_marca()}")
        print(f"Modelo: {self.get_modelo()}")
        print(f"Número de puertas: {self.__num_puertas}")
        print(f"Coste: {self.calcular_coste()} €")

    # Implementación del método abstracto
    def calcular_coste(self):
        return 150


# CLASE HIJA: Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.__cilindrada = cilindrada

    # Getter
    def get_cilindrada(self):
        return self.__cilindrada

    # Setter
    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    # Polimorfismo
    def mostrar_info(self):
        print("=== MOTO ===")
        print(f"Marca: {self.get_marca()}")
        print(f"Modelo: {self.get_modelo()}")
        print(f"Cilindrada: {self.__cilindrada} cc")
        print(f"Coste: {self.calcular_coste()} €")

    # Implementación del método abstracto
    def calcular_coste(self):
        return 80


# PROGRAMA PRINCIPAL
def main():
    # Crear objetos
    coche1 = Coche("Seat", "Ibiza", 5)
    coche2 = Coche("Renault", "Megane", 3)
    moto1 = Moto("Yamaha", "XMAX", 300)
    moto2 = Moto("Honda", "CBR", 500)

    # Lista de vehículos
    vehiculos = [coche1, coche2, moto1, moto2]

    # Mostrar información (polimorfismo)
    print("=== LISTADO DE VEHÍCULOS ===\n")

    for vehiculo in vehiculos:
        vehiculo.mostrar_info()
        print("----------------------------")


# Ejecutar
if __name__ == "__main__":
    main()