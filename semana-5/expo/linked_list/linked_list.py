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

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        self_str = "[ "

        current = self.head
        while current is not None:
            if current.next is not None:
                self_str += f"{str(current.data)}, "
            else:
                self_str += f"{str(current.data)} ]"
            current = current.next

        return self_str

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
            if current.next is not None:
                current = current.next
            else:
                current.next = new_node
                self.size += 1
                return

    def update_node(self, index: int, new_data: T) -> None:
        """
        Actualiza el valor de un nodo en la lista.
        """

        if self.is_empty():
            raise IndexError("Índice inválido: no hay elementos en la lista.")
        if index < 0:
            raise IndexError("Índice inválido: debe ser mayor o igual a cero.")
        if index >= self.size:
            raise IndexError(
                "Índice inválido: es fuera de límites; no corresponde a un nodo."
            )

        i = 0
        current = self.head
        while current is not None and i < index:
            i += 1
            current = current.next

        if current is not None:
            current.data = new_data

    def search(self, data: T) -> Optional[Node]:
        """
        Busca el valor de un nodo en la lista.
        """

        if self.is_empty():
            return None

        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next

        return None

    def delete(self, data: T, count: int = 1) -> None:
        """
        Elimina nodos con el valor especificado.
        """

        if self.is_empty():
            return
        if self.size == 1:
            self.head = None

        deletions = 0
        previous = None
        current = self.head

        while current is not None and deletions < count:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                deletions += 1

            previous = current
            current = current.next

    def delete_first(self) -> None:
        """
        Elimina el primer nodo de la lista.
        """

        if self.is_empty():
            return

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next

    def delete_last(self) -> None:
        """
        Elimina el último nodo de la lista.
        """

        if self.is_empty():
            return
        if self.size == 1:
            self.delete_first()
            return

        previous = None
        current = self.head

        while True:
            if current.next is None:
                previous.next = None
                return
            previous = current
            current = current.next
