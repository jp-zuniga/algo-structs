"""
Implementación personalizada de una pila como estructura de datos.
"""

from typing import Generic, Iterable, Optional, TypeVar

T = TypeVar("T")


class Pila(Generic[T]):
    """
    Estructura de datos lineal: último en entrar, primero en salir.
    """

    def __init__(self, valores: Optional[Iterable[T]] = None) -> None:
        if valores is None:
            self.valores = []
        else:
            self.valores = list(valores)

    def __len__(self) -> int:
        return len(self.valores)

    def __str__(self) -> str:
        return str(self.valores)

    def is_empty(self) -> bool:
        """
        Comprueba si la lista de valores esta vacía.
        """

        return len(self) == 0

    def add(self, valor: T) -> None:
        """
        Agrega un valor a la pila.
        """

        self.valores.append(valor)

    def extract(self) -> T:
        """
        Extrae el último valor de la pila y lo retorna.
        """

        return self.valores.pop()
