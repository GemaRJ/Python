class PlazasAgotadasError(Exception):
    """
    Excepción personalizada que se lanza cuando se intenta
    realizar una reserva en una actividad sin plazas disponibles.
    """
    pass


class UsoClaseAbstractaError(Exception):
    """
    Excepción personalizada que se lanza cuando se intenta
    instanciar o utilizar incorrectamente una clase abstracta.
    """
    pass
