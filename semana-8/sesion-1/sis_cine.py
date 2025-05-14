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
        str_sis = "["
        str_fila = str(self.fila_clientes)[1:-1].strip('"{').split("},")

        for i, elem in enumerate(str_fila):
            str_sis += f"\n    {i + 1}. [ {elem} ],"

        str_sis += "\n]"
        return str_sis


    def agregar_cliente(self, nuevo: Cliente) -> None:
        """
        Agrega un nuevo cliente al final de la fila/cola.
        """

        self.fila_clientes.enqueue(nuevo)

    def siguiente_cliente(self) -> Cliente:
        """
        Retorna el siguiente cliente a atender en la fila.
        """

        return self.fila_clientes.peek()

    def atender_cliente(self) -> Cliente:
        """
        Atiende al próximo cliente y lo elimina de la cola.
        """

        return self.fila_clientes.dequeue()
