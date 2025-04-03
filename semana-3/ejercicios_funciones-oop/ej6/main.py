"""
Crear una clase Factura que simule el proceso de facturación de una venta.
Los estudiantes deberán encapsular los datos internos de la factura
(como los detalles de los productos, cantidades, precios y descuentos)
y proveer métodos para calcular el total de la venta, generar
reportes simples y validar la integridad de la información.
"""

from clientes import (  # type: ignore # pylint: disable=E0401
    Cliente,
    ClienteOro,
    ClientePlatino
)

from factura import Factura  # type: ignore # pylint: disable=E0401
from producto import Producto  # type: ignore # pylint: disable=E0401


def main() -> None:
    """
    Ejecución del programa.
    """

    cliente1 = Cliente("0001", "Juancito Pérez", "7945-9316")
    cliente2 = ClienteOro("0002", "Juanita X", "1243-6549")
    cliente3 = ClientePlatino("0003", "Persona Random", "8764-9842")

    productos1 = [
        Producto(100, "Calculadora", 2, 123.4),
        Producto(101, "Laptop", 1, 2345.6),
        Producto(102, "Borrador", 3, 45.6),
    ]

    productos2 = [
        Producto(103, "iPhone", 1, 3456.7),
        Producto(104, "Galaxy S24", 1, 2345.6),
        Producto(105, "Galaxy Buds", 2, 1234.5),
    ]

    productos3 = [
        Producto(106, "Mochila", 1, 123.4),
        Producto(107, "Cuaderno", 3, 78.9),
        Producto(108, "Lapicero", 3, 45.6),
    ]

    factura1 = Factura("001", cliente1, productos1)
    factura2 = Factura("002", cliente2, productos2)
    factura3 = Factura("003", cliente3, productos3)

    print()
    print(factura1.generar_reporte())
    print()
    print(factura2.generar_reporte())
    print()
    print(factura3.generar_reporte())


if __name__ == "__main__":
    main()
