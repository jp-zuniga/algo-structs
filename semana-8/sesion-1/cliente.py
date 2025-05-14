"""
Implementación de la clase Cliente.
"""

class Cliente:
    """
    Representa un cliente de un cine.
    """

    def __init__(self, boleto: str, nombre_cliente: str, pelicula: str):
        self.datos: dict[str, str] = {
            "ID de Boleto": boleto,
            "Nombre de Cliente": nombre_cliente,
            "Película": pelicula
        }

    def __str__(self) -> str:
        return str(self.datos)
