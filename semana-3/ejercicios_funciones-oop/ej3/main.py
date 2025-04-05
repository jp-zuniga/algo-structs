"""
Desarrollar un programa para organizar diferentes algoritmos de búsqueda
en un paquete estructurado. Los estudiantes deberán crear al menos dos
módulos que contengan implementaciones de búsqueda lineal y búsqueda
binaria, configurando adecuadamente el archivo init.py. Posteriormente,
desde un script principal, se utilizarán estas funciones para
localizar elementos específicos en una colección de datos.
"""

from algoritmos import (
    busqueda_binaria,
    busqueda_lineal
)


def demostrar_busquedas():
    """
    Demostración de algoritmos.
    """

    # Datos de ejemplo
    numeros_desordenados = [45, 12, 85, 32, 89, 39, 69, 44, 42, 1, 6, 8]
    numeros_ordenados = sorted(numeros_desordenados)

    print("Lista desordenada:", numeros_desordenados)
    print("Lista ordenada:", numeros_ordenados)
    print("-" * 50)

    # Elemento a buscar
    elemento = 42

    # Demostración de búsqueda lineal
    print(f"Buscando el elemento {elemento} con búsqueda lineal:")
    indice = busqueda_lineal(numeros_desordenados, elemento)

    if indice != -1:
        print(f"Elemento encontrado en la posición {indice}")
    else:
        print("Elemento no encontrado")

    # Demostración de búsqueda binaria
    print(f"\nBuscando el elemento {elemento} con búsqueda binaria:")

    # Notar que usamos la lista ordenada para la búsqueda binaria
    indice = busqueda_binaria(numeros_ordenados, elemento)

    if indice != -1:
        print(f"Elemento encontrado en la posición {indice}")
    else:
        print("Elemento no encontrado")

    # Demostración con un elemento que no existe
    elemento_ausente = 99
    print(f"\nBuscando el elemento {elemento_ausente} que no existe:")

    indice_lineal = busqueda_lineal(numeros_desordenados, elemento_ausente)
    print(
        "Búsqueda lineal: " +
        f"{'No encontrado' if indice_lineal == -1 else f'Posición {indice_lineal}'}"
    )

    indice_binario = busqueda_binaria(numeros_ordenados, elemento_ausente)
    print(
        "Búsqueda binaria:" +
        f"{'No encontrado' if indice_binario == -1 else f'Posición {indice_binario}'}"
    )


if __name__ == "__main__":
    demostrar_busquedas()
