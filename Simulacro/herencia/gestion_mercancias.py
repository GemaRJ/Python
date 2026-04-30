# PROGRAMA: gestion_mercancias.py
# DESCRIPCIÓN:
# Programa para gestionar mercancías de una empresa de alimentación
# usando Programación Orientada a Objetos.
# Se trabaja con:
# - Herencia
# - Encapsulación
# - Polimorfismo
# - Abstracción

from abc import ABC, abstractmethod


# CLASE BASE ABSTRACTA: Mercancia
# Esta clase contiene los atributos comunes a todas las mercancías
class Mercancia(ABC):
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

    # Método para mostrar información general
    def mostrar_info(self):
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")

    # Método abstracto: obliga a las clases hijas a implementarlo
    @abstractmethod
    def calcular_coste(self):
        pass


# CLASE HIJA: Fruta
# Hereda de Mercancia y añade el atributo procedencia
class Fruta(Mercancia):
    def __init__(self, marca, modelo, procedencia):
        super().__init__(marca, modelo)
        self.__procedencia = procedencia

    # Getter de procedencia
    def get_procedencia(self):
        return self.__procedencia

    # Setter de procedencia
    def set_procedencia(self, procedencia):
        self.__procedencia = procedencia

    # Sobrescritura del método mostrar_info (polimorfismo)
    def mostrar_info(self):
        print("=== FRUTA ===")
        print(f"Marca: {self.get_marca()}")
        print(f"Modelo: {self.get_modelo()}")
        print(f"Procedencia: {self.__procedencia}")
        print(f"Coste: {self.calcular_coste()} €")

    # Implementación del método abstracto
    def calcular_coste(self):
        return 10


# CLASE HIJA: Carne
# Hereda de Mercancia y añade el atributo animal
class Carne(Mercancia):
    def __init__(self, marca, modelo, animal):
        super().__init__(marca, modelo)
        self.__animal = animal

    # Getter de animal
    def get_animal(self):
        return self.__animal

    # Setter de animal
    def set_animal(self, animal):
        self.__animal = animal

    # Sobrescritura del método mostrar_info (polimorfismo)
    def mostrar_info(self):
        print("=== CARNE ===")
        print(f"Marca: {self.get_marca()}")
        print(f"Modelo: {self.get_modelo()}")
        print(f"Animal: {self.__animal}")
        print(f"Coste: {self.calcular_coste()} €")

    # Implementación del método abstracto
    def calcular_coste(self):
        return 20


# PROGRAMA PRINCIPAL
def main():
    # Crear varios objetos
    fruta1 = Fruta("Fresh", "Manzana Golden", "España")
    fruta2 = Fruta("Tropic", "Plátano Premium", "Canarias")
    carne1 = Carne("Cárnicas Sur", "Solomillo", "Ternera")
    carne2 = Carne("Granja Norte", "Pechuga", "Pollo")

    # Guardar los objetos en una lista
    mercancias = [fruta1, fruta2, carne1, carne2]

    # Recorrer la lista mostrando la información
    # Aquí se usa polimorfismo, porque cada objeto responde
    # a mostrar_info() de forma distinta
    print("=== LISTADO DE MERCANCÍAS ===\n")

    for mercancia in mercancias:
        mercancia.mostrar_info()
        print("----------------------------")


# Ejecutar el programa
if __name__ == "__main__":
    main()