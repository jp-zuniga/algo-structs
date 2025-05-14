"""
Implementación de la clase Cola.
"""

from typing import Generic, Iterable, Optional, TypeVar

T = TypeVar("T")


class Cola(Generic[T]):
    """
    Implementación personalizada de una cola.
    """

    def __init__(self, elementos: Optional[Iterable[T]] = None) -> None:
        if elementos is None:
            self.elementos = []
        else:
            self.elementos = list(elementos)

    def __len__(self) -> int:
        return len(self.elementos)

    def __str__(self) -> str:
        return str([str(elem) for elem in self.elementos])

    def is_empty(self) -> bool:
        """
        Comprueba si la cola esta vacía.
        """
        return len(self) == 0

    def check_front(self) -> T:
        """
        Retorna el primer elemento de la cola.
        """

        return self.elementos[0]

    def enqueue(self, elem: T) -> None:
        """
        Agrega un elemento a la cola.
        """

        self.elementos.append(elem)

    def dequeue(self) -> T:
        """
        Elimina y retorna el primer elemento de la cola.
        """

        return self.elementos.pop(0)
