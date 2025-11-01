class LongitudMatriculaNoValidaException(Exception):
    def __init__(self):
        super().__init__("La matrícula debe tener exactamente 7 caracteres.")


class FormatoMatriculaNoValidoException(Exception):
    def __init__(self):
        super().__init__("Los últimos 3 caracteres de la matrícula deben ser letras.")