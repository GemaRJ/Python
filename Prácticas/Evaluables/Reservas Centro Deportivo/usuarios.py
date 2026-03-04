from abc import ABC, abstractmethod


# CLASE BASE ABSTRACTA USUARIO

class Usuario(ABC):
    """
    Clase abstracta base para todos los usuarios del centro deportivo.
    No se puede instanciar directamente.
    """

    def __init__(self, nombre, email):
        if type(self) is Usuario:
            raise TypeError("No se puede instanciar la clase Usuario directamente")
        self._nombre = nombre
        self._email = email

    @abstractmethod
    def tipo_usuario(self):
        """
        Método abstracto que debe implementarse en las subclases.
        Retorna el tipo de usuario (Cliente o Entrenador).
        """
        pass

  
    # MÉTODOS GET
   
    def get_nombre(self):
        """Devuelve el nombre del usuario"""
        return self._nombre

    def get_email(self):
        """Devuelve el email del usuario"""
        return self._email

# CLASE CLIENTE

class Cliente(Usuario):
    """
    Representa a un cliente del centro deportivo.
    Puede realizar reservas y consultar las mismas.
    """

    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self._reservas = []  # Lista de reservas asociadas al cliente

    def tipo_usuario(self):
        """Devuelve 'Cliente' como tipo de usuario"""
        return "Cliente"

    def añadir_reserva(self, reserva):
        """Añade una reserva a la lista del cliente"""
        self._reservas.append(reserva)

    def mostrar_reservas(self):
        """Muestra todas las reservas del cliente"""
        if not self._reservas:
            print("No tienes reservas.")
        else:
            for reserva in self._reservas:
                reserva.mostrar_info()


# CLASE ENTRENADOR

class Entrenador(Usuario):
    """
    Representa a un entrenador del centro deportivo.
    Puede estar asociado a actividades y tiene una especialidad.
    """

    def __init__(self, nombre, email, especialidad):
        super().__init__(nombre, email)
        self._especialidad = especialidad  # Especialidad del entrenador

    def tipo_usuario(self):
        """Devuelve 'Entrenador' como tipo de usuario"""
        return "Entrenador"

    def get_especialidad(self):
        """Devuelve la especialidad del entrenador"""
        return self._especialidad
