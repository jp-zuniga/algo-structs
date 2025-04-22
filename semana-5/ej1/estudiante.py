"""
Implementación de la clase Estudiante.
"""

class Estudiante:
    """
    Representa los datos de un estudiante.
    """

    def __init__(
        self,
        carnet: str,
        nombres: tuple[str, str],
        apellidos: tuple[str, str],
        genero: str,
        peso: float,
        estatura: float,
        promedio: float
    ) -> None:
        self.carnet = carnet
        self.nombres = nombres
        self.apellidos = apellidos
        self.genero = genero
        self.peso = peso
        self.estatura = estatura
        self.promedio = promedio
