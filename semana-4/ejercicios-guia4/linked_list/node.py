"""
Implementación de un nodo en una lista enlazada.
"""

from typing import Any, Optional


class Node:
    """
    Representa un nodo en una lista enlazada,
    con el dato que almacena, y el proximo elemento en la lista.
    """

    def __init__(self, data: Any, next_node: Optional["Node"] = None):
        self.data = data
        self.next = next_node
