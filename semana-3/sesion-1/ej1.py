"""
Ejercicio de funciones con Python: suma, menor y mayor de los números.
"""


def suma(lista: list[int]) -> int:
    """
    Retorna la suma de todos los números en una lista de enteros.
    """

    total = 0
    for num in lista:
        total += num

    return total


def mayor(lista: list[int]) -> int:
    """
    Retorna el número más grande en una lista de enteros.
    """

    maximo = 0
    for num in lista:
        # la funcion max() tambien acepta argumentos de
        # lista e itera sobre ella de esta misma manera
        maximo = max(maximo, num)

    return maximo


def menor(lista: list[int]) -> int:
    """
    Retorna el número más pequeño en una lista de enteros.
    """

    minimo = lista[0]
    for num in lista:
        # la funcion min() tambien acepta argumentos de
        # lista e itera sobre ella de esta misma manera
        minimo = min(minimo, num)

    return minimo


def main() -> None:
    """
    Ejecución del programa.
    """

    lista = []
    n = int(input("\nIngrese la cantidad de elementos a procesar: "))

    print()

    for i in range(n):
        lista.append(int(input(f"Ingrese el elemento #{i + 1}: ")))

    print(f"\nElementos de la lista: {lista}")
    print(f"Suma de los elementos de la lista: {suma(lista)}")
    print(f"Número más grande de la lista: {mayor(lista)}")
    print(f"Número más pequeño de la lista: {menor(lista)}\n")


if __name__ == "__main__":
    main()
