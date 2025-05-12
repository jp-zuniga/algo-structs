"""
Implementación de la clase Cliente.
"""

class Cliente:
    """
    Representa un cliente de un cine.
    """

    def __init__(self, pelicula: str, boleto: str):
        self.pelicula = pelicula
        self.boleto = boleto

    def __str__(self) -> str:
        return f"[ Película: {self.pelicula}; ID de Boleto: {self.boleto} ]"

    def validar_boleto(self) -> bool:
        """
        Si el nombre de la película está en el boleto, es válido.
        """

        return self.pelicula in self.boleto
