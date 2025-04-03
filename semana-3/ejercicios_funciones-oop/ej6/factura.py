"""
Definición de la clase Factura.
"""

from typing import Union
from clientes import (  # type: ignore # pylint: disable=E0401
    Cliente,
    ClienteOro,
    ClientePlatino
)

from producto import Producto  # type: ignore # pylint: disable=E0401


class Factura:
    """
    Representa una factura.
    """

    def __init__(
        self,
        codigo: str,
        cliente: Union[Cliente, ClienteOro, ClientePlatino],
        productos: list[Producto]
    ):
        self.codigo = codigo
        self.cliente = cliente
        self.productos = productos

    def get_producto_str(self) -> str:
        """
        Convierte la lista de productos a un string para imprimir.
        """

        return "\n".join(str(p) for p in self.productos)

    def calcular_total(self) -> float:
        """
        Suma todos los montos de todos los productos en
        self.productos y le aplica el descuento del cliente.
        """

        return sum(
            p.precio * p.cantidad for p in self.productos
        ) * self.cliente.descuento

    def generar_reporte(self) -> str:
        """
        Organiza los datos de la factura para imprimirlos.
        """

        total = self.calcular_total()
        subtotal = total * (1 - self.cliente.descuento + 1)
        reporte = ""

        reporte += "=" * 50
        reporte += f"\nFACTURA #{self.codigo}\n"
        reporte += "=" * 50

        reporte += "\nDATOS DEL CLIENTE:\n"
        reporte += "-" * 50
        reporte += f"\nNombre: {self.cliente.nombre}"
        reporte += f"\nNúmero de teléfono: {self.cliente.telefono}"
        reporte += f"\nDescuento aplicable: {(1 - self.cliente.descuento) * 100:.0f}%\n"

        reporte += "-" * 50
        reporte += "\nPRODUCTOS:\n"
        reporte += "-" * 50
        reporte += "\n" + self.get_producto_str()

        reporte += "\n" + "=" * 50
        reporte += f"\nSUBTOTAL: C${subtotal:.2f}"
        reporte += f"\nDESCUENTO: {(1 - self.cliente.descuento) * 100:.0f}%"
        reporte += f"\nTOTAL A PAGAR: C${total:.2f}\n"
        reporte += "=" * 50
        reporte += "\n"

        return reporte
