"""
Implementación personalizada de una lista enlazada.
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


class LinkedList:
    """
    Implementación personalizada de una lista enlazada.
    """

    def __init__(self):
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        current = self.head

        list_str = "[ "
        while current is not None:
            list_str += f"{current.data}{"," if current.next is not None else ""}"
        list_str += " ]"

        return list_str

    def is_empty(self) -> bool:
        """
        Determina si la lista esta vacía.
        """

        return self.head is None

    def add_at_front(self, data: Any) -> None:
        """
        Agrega un nuevo elemento al inicio de la lista enlazada.
        """

        self.head = Node(data=data, next_node=self.head)

    def add_at_end(self, data: Any) -> None:
        """
        Agrega un nuevo elemento al final de la lista enlazada.
        """

        if self.is_empty():
            self.head = Node(data)
            return

        current = self.head
        while current is not None:
            current = current.next
        current.next = data

    def search(self, data: Any) -> Optional[Node]:
        """
        Busca el valor de un nodo en la lista.
        """

        elem_actual = self.head

        while True:
            if elem_actual.data == data:
                return elem_actual
            if elem_actual.next is None:
                return None

            elem_actual = elem_actual.next

    def delete(self, data: Any) -> bool:
        """
        Elimina el valor de un nodo.
        """

        current = self.head
        previous = None

        while current is not None and current.data != data:
            previous = current
            current = current.next
            if previous is None:
                self.head = current.next
            elif current is not None:
                previous.next = current.next
                current.next = None

        return True
