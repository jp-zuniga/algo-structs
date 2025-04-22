"""
Construir un método encontrar_vocales() que determine la
cantidad de vocales almacenadas en una lista de caracteres.
"""

from linked_list import LinkedList


def encontrar_vocales(lista: LinkedList[str]) -> int:
    """
    Encuentra la cantidad de vocales en una lista enlazada de caracteres.
    """

    cantidad = 0
    current = lista.head

    while current is not None:
        if current.data in ("a", "e", "i", "o", "u"):
            cantidad += 1
        current = current.next

    return cantidad


def main() -> None:
    """
    Ejecución del programa.
    """

    lista: LinkedList[str] = LinkedList()

    print()
    while True:
        elemento = input(
            "Ingrese el caracter que desea agregar a la lista (dejar vacío para terminar): "
        )

        if elemento == "":
            break

        lista.add_at_end(elemento)

    print("\n-------------------------------------------\n")
    print(f"Cantidad de vocales en lista: {encontrar_vocales(lista)}\n")


if __name__ == "__main__":
    main()
