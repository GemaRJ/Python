from abc import ABC, abstractmethod
from excepciones import PlazasAgotadasError


# CLASE ABSTRACTA ACTIVIDAD

class Actividad(ABC):
    """
    Clase abstracta base para todas las actividades del centro deportivo.
    No se puede instanciar directamente.
    """

    def __init__(self, nombre, precio_base, plazas_maximas):
        # Evita instanciar directamente la clase abstracta
        if type(self) is Actividad:
            raise TypeError("No se puede instanciar Actividad directamente")

        self._nombre = nombre                    # Nombre de la actividad
        self._precio_base = precio_base          # Precio base de la actividad
        self._plazas_maximas = plazas_maximas    # Número máximo de plazas
        self._plazas_ocupadas = 0                # Plazas ocupadas inicialmente

    def hay_plazas(self):
        """
        Comprueba si quedan plazas disponibles.
        Devuelve True si hay plazas libres, False en caso contrario.
        """
        return self._plazas_ocupadas < self._plazas_maximas

    def ocupar_plaza(self):
        """
        Incrementa el número de plazas ocupadas.
        Lanza una excepción si no quedan plazas disponibles.
        """
        if not self.hay_plazas():
            raise PlazasAgotadasError("No hay plazas disponibles para esta actividad")
        self._plazas_ocupadas += 1

    def get_estado_ocupacion(self):
        """
        Devuelve el estado de ocupación de la actividad
        en formato: plazas_ocupadas/plazas_maximas
        """
        return f"{self._plazas_ocupadas}/{self._plazas_maximas}"

    def get_nombre(self):
        """Devuelve el nombre de la actividad"""
        return self._nombre

    @abstractmethod
    def calcular_precio(self):
        """
        Método abstracto que calcula el precio final de la actividad.
        Debe implementarse en las subclases.
        """
        pass


# CLASE CLASE COLECTIVA

class ClaseColectiva(Actividad):
    """
    Representa una actividad grupal con precio fijo.
    """

    def calcular_precio(self):
        """Devuelve el precio base de la actividad"""
        return self._precio_base


# CLASE ENTRENAMIENTO PERSONAL

class EntrenamientoPersonal(Actividad):
    """
    Representa una actividad personalizada con un recargo porcentual
    sobre el precio base.
    """

    def __init__(self, nombre, precio_base, plazas_maximas, recargo_porcentaje):
        super().__init__(nombre, precio_base, plazas_maximas)
        self._recargo_porcentaje = recargo_porcentaje  # Porcentaje de recargo

    def calcular_precio(self):
        """
        Calcula el precio final aplicando el recargo porcentual
        sobre el precio base.
        """
        return self._precio_base * (1 + self._recargo_porcentaje / 100)
