"""
Implementación de un nodo en una lista enlazada.
"""

from typing import (
    Generic,
    Optional,
    TypeVar
)

T = TypeVar("T")


class Node(Generic[T]):
    """
    Representa un nodo en una lista enlazada,
    con el dato que almacena, y el proximo elemento en la lista.
    """

    def __init__(self, data: T, next_node: Optional["Node"] = None):
        self.data = data
        self.next = next_node
