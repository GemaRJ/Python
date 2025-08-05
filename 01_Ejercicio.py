
# Importamos las excepciones personalizadas desde el archivo excepciones.py
from exception import LongitudMatriculaNoValidaException, FormatoMatriculaNoValidoException

# Definimos la clase RegistroVehiculo
class RegistroVehiculo:
    # Constructor de la clase. Inicializa los atributos del vehículo
    def __init__(self, matricula="", marca="", anio=0):
        self.matricula = matricula
        self.marca = marca
        self.anio = anio

    # Método para establecer la matrícula, con validaciones
    def set_matricula(self, matricula):
        # Comprobamos si la matrícula tiene exactamente 7 caracteres
        if len(matricula) != 7:
            raise LongitudMatriculaNoValidaException()
        # Comprobamos si los últimos 3 caracteres son letras
        if not matricula[-3:].isalpha():
            raise FormatoMatriculaNoValidoException()
        self.matricula = matricula

    # Método para establecer la marca del vehículo
    def set_marca(self, marca):
        self.marca = marca

    # Método para establecer el año de matriculación
    def set_anio(self, anio):
        self.anio = anio

    # Método para comprobar si todos los datos están completos
    def esta_completo(self):
        return self.matricula != "" and self.marca != "" and self.anio != 0

    # Método para mostrar por pantalla los datos del vehículo
    def mostrar_datos(self):
        print("\n--- Datos del vehículo registrados ---")
        print(f"Matrícula: {self.matricula}")
        print(f"Marca: {self.marca}")
        print(f"Año de matriculación: {self.anio}")
