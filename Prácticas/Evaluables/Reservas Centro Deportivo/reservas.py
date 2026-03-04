class Reserva:
    """
    Representa la reserva de una actividad realizada por un cliente.
    Al crear la reserva:
    - Se calcula el precio final de la actividad
    - Se ocupa una plaza en la actividad
    - Se añade la reserva al cliente
    """

    def __init__(self, cliente, actividad):
        self._cliente = cliente          # Cliente que realiza la reserva
        self._actividad = actividad      # Actividad reservada

        # Cálculo del precio final según el tipo de actividad
        self._precio_final = actividad.calcular_precio()

        # Se comprueba disponibilidad y se ocupa una plaza
        actividad.ocupar_plaza()

        # Se añade la reserva al historial del cliente
        cliente.añadir_reserva(self)

    def mostrar_info(self):
        """
        Muestra por pantalla la información detallada de la reserva.
        """
        print("Actividad:", self._actividad.get_nombre())
        print("Precio final:", round(self._precio_final, 2), "€")
        print("Ocupación:", self._actividad.get_estado_ocupacion())
        print("-" * 30)
