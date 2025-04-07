"""
Aplicación que permite a un usuario, principalmente estudiantes,
registrar sus gastos para llevar mejor control sobre ellos.
"""

from .gasto import Gasto
from .manejo_gastos import (
    agregar_gasto,
    encontrar_total,
    mostrar_gastos,
    promediar_categoria
)


__all__ = [
    "Gasto",
    "agregar_gasto",
    "encontrar_total",
    "mostrar_gastos",
    "promediar_categoria"
]
