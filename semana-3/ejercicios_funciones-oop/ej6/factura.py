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
        self.__codigo = codigo
        self.__cliente = cliente
        self.__productos = productos

    @property
    def codigo(self) -> str:
        """
        Getter para el atributo protegido __codigo.
        """

        return self.__codigo

    @property
    def cliente(self) -> Union[Cliente, ClienteOro, ClientePlatino]:
        """
        Getter para el atributo protegido __cliente.
        """

        return self.__cliente

    @property
    def productos(self) -> list[Producto]:
        """
        Getter para el atributo protegido __productos.
        """

        return self.__productos

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

        reporte += "=" * 75
        reporte += f"\nFACTURA #{self.codigo}\n"
        reporte += "=" * 75

        reporte += "\nDATOS DEL CLIENTE:\n"
        reporte += "-" * 75
        reporte += f"\nNombre: {self.cliente.nombre}"
        reporte += f"\nNúmero de teléfono: {self.cliente.telefono}"
        reporte += f"\nDescuento aplicable: {(1 - self.cliente.descuento) * 100:.0f}%\n"

        reporte += "-" * 75
        reporte += "\nPRODUCTOS:\n"
        reporte += "-" * 75
        reporte += "\n" + self.get_producto_str()

        reporte += "\n" + "=" * 75
        reporte += f"\nSUBTOTAL: C${subtotal:.2f}"
        reporte += f"\nDESCUENTO: {(1 - self.cliente.descuento) * 100:.0f}%"
        reporte += f"\nTOTAL A PAGAR: C${total:.2f}\n"
        reporte += "=" * 75
        reporte += "\n"

        return reporte
