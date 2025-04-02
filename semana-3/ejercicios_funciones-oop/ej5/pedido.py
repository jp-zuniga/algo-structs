"""
Definición de la clase Pedido.
"""

from typing import Union
from clientes import (
    Cliente,
    ClienteOro,
    ClientePlatino
)

from producto import Producto  # pylint: disable=E0401


class Pedido:
    """
    Representa una compra.
    """

    def __init__(
        self,
        cliente: Union[Cliente, ClienteOro, ClientePlatino],
        productos: list[Producto]
    ):
        self.cliente = cliente
        self.productos = productos
        self.total = self._calcular_total()

    def _calcular_total(self) -> float:
        return sum(
            p.precio * p.cantidad for p in self.productos
        ) * self.cliente.descuento

    def get_producto_str(self) -> str:
        """
        Convierte la lista de productos a un string para imprimir.
        """

        return "\n".join(str(p) for p in self.productos)
