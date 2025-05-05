"""
Implementación de la clase Paciente.
"""

class Paciente:
    """
    Representa los datos de un paciente médico.
    """

    def __init__(
        self,
        nombre: str,
        edad: int,
        sintoma: str,
        prioridad: int
    ) -> None:
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma
        self.prioridad = prioridad
