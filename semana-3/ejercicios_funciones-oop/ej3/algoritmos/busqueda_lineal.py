"""
Algoritmo de búsqueda lineal.
"""


def busqueda_lineal(coleccion, elemento):
    """
    Implementa el algoritmo de búsqueda lineal.
    """

    for i, elem in enumerate(coleccion):
        if elem == elemento:
            return i

    return -1
