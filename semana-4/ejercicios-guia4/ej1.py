"""
Implementar un método que recibe una lista de enteros L y un número
entero n de forma que modifique la lista mediante el borrado de
todos los elementos de la lista que tengan este valor.
"""

from linked_list import LinkedList


def main() -> None:
    """
    Ejecución del programa.
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

        lista.add_at_end(int(elemento))

    while True:
        n = input("Ingrese el valor a eliminar de la lista: ")
        if not n.isnumeric():
            input("\n¡Error! String ingresado no es un número, intente nuevamente...")
            continue
        break

    # delete() esta implementado para eliminar
    # todos los nodos con el valor especificado
    lista.delete(int(n))
    print("\n-------------------------------------------\n")
    print(f"{lista}\n")


if __name__ == "__main__":
    main()
