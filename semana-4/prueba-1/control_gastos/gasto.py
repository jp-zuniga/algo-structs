"""
Implementación de la clase Gasto.
"""

from datetime import date


class Gasto:
    """
    Representa un gasto monetario mensual.
    """

    _categorias = [
        "alimentos",
        "renta",
        "transporte",
    ]

    def __init__(
        self,
        codigo: int,
        fecha: date,
        categoria: str,
        monto: float,
        descripcion: str
    ):
        self._codigo = codigo
        self._fecha = fecha
        self._categoria = categoria
        self._monto = monto
        self._descripcion = descripcion

    @property
    def fecha(self) -> date:
        """
        Getter method para acceder al atributo privado _fecha.
        """

        return self._fecha

    @property
    def categoria(self) -> str:
        """
        Getter method para acceder al atributo privado _categoria.
        """

        return self._categoria

    @property
    def monto(self) -> float:
        """
        Getter method para acceder al atributo privado _monto.
        """

        return self._monto

    @property
    def descripcion(self) -> str:
        """
        Getter method para acceder al atributo privado _descripcion.
        """

        return self._descripcion

    @staticmethod
    def categorias() -> list[str]:
        """
        Getter method para acceder al atributo privado _categorias.
        """

        return Gasto._categorias

    @classmethod
    def agregar_categoria(cls, cat_nueva: str) -> None:
        """
        Agrega la categoría dada a la lista de categorías válidas.
        """

        cls._categorias.append(cat_nueva)

    @classmethod
    def validar_categoria(cls, cat: str) -> bool:
        """
        Valida si un string es una categoría de gasto válida.
        """

        return cat in cls._categorias
