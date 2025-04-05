"""
Algoritmo de búsqueda binaria.
"""


def busqueda_binaria(coleccion, elemento):
    """
    Implementa el algoritmo de búsqueda binaria.
    Requiere que la colección esté ordenada.
    """

    izquierda, derecha = 0, len(coleccion) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        # Verificar si el elemento está en el medio
        if coleccion[medio] == elemento:
            return medio

        # Si el elemento es mayor, ignorar la mitad izquierda
        if coleccion[medio] < elemento:
            izquierda = medio + 1

        # Si el elemento es menor, ignorar la mitad derecha
        else:
            derecha = medio - 1

    # Elemento no encontrado
    return -1
