"""
Implementación personalizada de una lista enlazada.
"""

from typing import (
    Generic,
    Optional,
    TypeVar
)

from .node import Node

T = TypeVar("T")


class LinkedList(Generic[T]):
    """
    Implementación personalizada de una lista enlazada.
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        current = self.head
        elements = []

        while current is not None:
            elements.append(str(current.data))
            current = current.next

        return f"[ {", ".join(elements)} ]"

    def is_empty(self) -> bool:
        """
        Determina si la lista esta vacía.
        """

        return self.head is None

    def add_at_front(self, data: T) -> None:
        """
        Agrega un nuevo elemento al inicio de la lista enlazada.
        """

        self.head = Node(data=data, next_node=self.head)
        self.size += 1

    def add_at_end(self, data: T) -> None:
        """
        Agrega un nuevo elemento al final de la lista enlazada.
        """

        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.size += 1
            return

        current = self.head
        while True:
            if current.next is not None:  # type: ignore
                current = current.next  # type: ignore
            else:
                current.next = new_node  # type: ignore
                self.size += 1
                return

    def search(self, data: T) -> Optional[Node]:
        """
        Busca el valor de un nodo en la lista.
        """

        current = self.head

        while current is not None:
            if current.data == data:
                return current
            current = current.next

        return None

    def delete(self, data: T) -> None:
        """
        Elimina todos los nodos con el valor especificado.
        """

        previous = None
        current = self.head

        while current is not None:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
            previous = current
            current = current.next
