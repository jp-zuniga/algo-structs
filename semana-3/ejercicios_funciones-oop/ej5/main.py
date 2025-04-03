"""
Crear una clase Cliente con atributos básicos (por ejemplo, ID, nombre y contacto)
y una clase Pedido que contenga información sobre el cliente, la lista de productos
solicitados y el total de la venta. Se podrá incluir el uso de herencia para diferenciar
entre tipos de clientes (regular, VIP, etc.) y aplicar descuentos especiales.
"""

from clientes import (
    Cliente,
    ClienteOro,
    ClientePlatino
)

from pedido import Pedido
from producto import Producto  # pylint: disable=E0401


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

    pedido1 = Pedido(cliente1, productos1)
    pedido2 = Pedido(cliente2, productos2)
    pedido3 = Pedido(cliente3, productos3)

    print("\nDatos de Pedido #1:")
    print(f"Cliente: {pedido1.cliente.nombre} ({pedido1.cliente.telefono})")
    print(f"Productos:\n{pedido1.get_producto_str()}")
    print(f"Total del pedido #1: {pedido1.total}")

    print("\nDatos de Pedido #2:")
    print(f"Cliente: {pedido2.cliente.nombre} ({pedido2.cliente.telefono})")
    print(f"Productos:\n{pedido2.get_producto_str()}")
    print(f"Total del pedido #2: {pedido2.total}")

    print("\nDatos de Pedido #3:")
    print(f"Cliente: {pedido3.cliente.nombre} ({pedido3.cliente.telefono})")
    print(f"Productos:\n{pedido3.get_producto_str()}")
    print(f"Total del pedido #3: {pedido3.total}")

    print()


if __name__ == "__main__":
    main()
