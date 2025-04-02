"""
Definición de la clase Producto.
"""


class Producto:
    """
    Clase de datos para representar un producto con:
    - un código,
    - un nombre,
    - una cantidad,
    - un precio
    """

    def __init__(
        self,
        codigo: int = 0,
        nombre: str = "",
        cantidad: int = 0,
        precio: float = 0.0
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self) -> str:
        return (
            f"Código: {self.codigo}, Nombre: {self.nombre}, " +
            f"Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"
        )
