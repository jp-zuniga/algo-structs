"""
Paquete que implementa algoritmos de busqueda (lineal y binaria).
"""

from .busqueda_lineal import busqueda_lineal
from .busqueda_binaria import busqueda_binaria


# Facilita la importación directa de las funciones
__all__ = [
    "busqueda_lineal",
    "busqueda_binaria"
]
