"""
Ejercicio #4.
"""

from .acciones_editor import (
    EscribirTexto,
    BorrarTexto,
    CopiarTexto,
    PegarTexto
)

from .editor import EditorTexto


__all__ = [
    "EditorTexto",
    "EscribirTexto",
    "BorrarTexto",
    "CopiarTexto",
    "PegarTexto",
]
