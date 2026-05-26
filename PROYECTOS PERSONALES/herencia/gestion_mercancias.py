# PROGRAMA: gestion_mercancias.py

# Importamos clases abstractas
from abc import ABC, abstractmethod

# Clase base abstracta
class Mercancia(ABC):

    # Constructor
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    # Getter marca
    def get_marca(self):
        return self.__marca

    # Setter marca
    def set_marca(self, marca):
        self.__marca = marca

    # Getter modelo
    def get_modelo(self):
        return self.__modelo

    # Setter modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo

    # Mostrar información general
    def mostrar_info(self):
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")

    # Método abstracto
    @abstractmethod
    def calcular_coste(self):
        pass


# Clase hija Fruta
class Fruta(Mercancia):

    # Constructor
    def __init__(self, marca, modelo, procedencia):
        super().__init__(marca, modelo)
        self.__procedencia = procedencia

    # Polimorfismo
    def mostrar_info(self):
        print("=== FRUTA ===")
        print(f"Marca: {self.get_marca()}")
        print(f"Modelo: {self.get_modelo()}")
        print(f"Procedencia: {self.__procedencia}")
        print(f"Coste: {self.calcular_coste()} €")

    # Implementación método abstracto
    def calcular_coste(self):
        return 10


# Clase hija Carne
class Carne(Mercancia):

    # Constructor
    def __init__(self, marca, modelo, animal):
        super().__init__(marca, modelo)
        self.__animal = animal

    # Polimorfismo
    def mostrar_info(self):
        print("=== CARNE ===")
        print(f"Marca: {self.get_marca()}")
        print(f"Modelo: {self.get_modelo()}")
        print(f"Animal: {self.__animal}")
        print(f"Coste: {self.calcular_coste()} €")

    # Implementación método abstracto
    def calcular_coste(self):
        return 20


# Programa principal
def main():

    # Crear objetos
    fruta1 = Fruta("Fresh", "Manzana Golden", "España")
    fruta2 = Fruta("Tropic", "Plátano Premium", "Canarias")

    carne1 = Carne("Cárnicas Sur", "Solomillo", "Ternera")
    carne2 = Carne("Granja Norte", "Pechuga", "Pollo")

    # Lista de mercancías
    mercancias = [fruta1, fruta2, carne1, carne2]

    # Mostrar mercancías
    print("=== LISTADO DE MERCANCÍAS ===\n")

    for mercancia in mercancias:
        mercancia.mostrar_info()
        print("----------------------------")


# Ejecutar programa
if __name__ == "__main__":
    main()











