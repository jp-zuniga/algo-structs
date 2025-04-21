"""
Construir un método imprime_inverso() que imprima los elementos de una lista
enlazada de enteros en orden inverso a partir de una posición p.
"""

from lista_enlazada import LinkedList


def imprimir_inverso(lista: LinkedList, p: int) -> None:
    """
    Imprime los elementos de una lista enlazada de
    enteros en orden inverso a partir de una posición p.
    """

    i = 0
    inversa = []
    current = lista.head

    while current.next is not None:  # type: ignore
        inversa.append(current.data)  # type: ignore
        current = current.next  # type: ignore
        i += 1

        if p == i:
            break

    print(f"{inversa[::-1]}\n")


def menu() -> None:
    """
    Loop principal del programa que le muestra un menú de opciones al usuario.
    """

    lista = LinkedList()
    print()

    while True:
        elemento = input(
            "Ingrese el elemento que desea agregar a la lista (dejar vacío para terminar): "
        )

        if elemento == "":
            break
        if not elemento.isnumeric():
            input("\n¡Error! Elemento ingresado no es un número, intente nuevamente...")
            continue

        lista.add_at_end(elemento)

    while True:
        p = input("Ingrese el índice a partir para imprimir los elementos en orden inverso: ")
        if not p.isnumeric():
            input("\n¡Error! String ingresado no es un número, intente nuevamente...")
            continue
        break

    print("\n-------------------------------------------\n")
    imprimir_inverso(lista, int(p))


def main() -> None:
    """
    Ejecución del programa.
    """

    menu()


if __name__ == "__main__":
    main()
