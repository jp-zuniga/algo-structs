"""
Definición de las clases Cliente, ClienteOro y ClientePlatino.
"""


class Cliente:
    """
    Representa un cliente del negocio y sus detalles.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        telefono: str
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono
        self.descuento = 1.0  # 0%


class ClienteOro(Cliente):
    """
    Representa un cliente 'Oro' del negocio,
    ue tiene un descuento de 15% en sus compras.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        telefono: str
    ):
        Cliente.__init__(self, codigo, nombre, telefono)
        self.descuento = 1.15  # 15%


class ClientePlatino(Cliente):
    """
    Representa un cliente 'Platino' del negocio,
    ue tiene un descuento de 30% en sus compras.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        telefono: str
    ):
        Cliente.__init__(self, codigo, nombre, telefono)
        self.descuento = 1.30  # 30%
