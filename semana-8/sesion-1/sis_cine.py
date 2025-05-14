"""
Implementación de la clase SisCine, que maneja la simulación de la fila.
"""

from . import Cliente, Cola


class SisCine:
    """
    Sistema para adminsitrar una fila de clientes en un cine, utilizando una cola.
    """

    def __init__(self, fila: Cola[Cliente]) -> None:
        self.fila_clientes = fila

    def __str__(self) -> str:
        return str(self.fila_clientes)

    def agregar_cliente(self, nuevo: Cliente) -> None:
        """
        Agrega un nuevo cliente al final de la fila/cola.
        """

        self.fila_clientes.enqueue(nuevo)

    def atender_cliente(self) -> Cliente:
        """
        Atiende al próximo cliente y lo elimina de la cola.
        """

        return self.fila_clientes.dequeue()
