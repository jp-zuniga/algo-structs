"""
Manejo de listas enlazadas.
"""

from os import system

from . import LinkedList


def menu() -> None:
    """
    Loop principal del programa que le muestra un menú de opciones al usuario.
    """

    opcion = ""
    lista = LinkedList()

    while opcion != "6":
        system("cls || clear")
        print("\nPrueba de LinkedList()")
        print("-----------------------------------------------------\n")
        print("1. Agregar")
        print("2. Buscar")
        print("3. Mostrar")
        print("4. Modificar")
        print("5. Eliminar")
        print("6. Salir")

        opcion = input("\n-> ")

        match opcion:
            case "1":
                lista.add_at_end(input("\nIngrese el nuevo dato: "))
                input("\n¡Elemento agregado exitosamente!")
            case "2":
                busqueda = lista.search(
                    input("\nIngrese el elemento que desea buscar en la lista: ")
                )

                if busqueda is None:
                    input("\n¡Error! Dato ingresado no existe en la lista...")
                else:
                    input(f"\nElemento: {busqueda.data}")
            case "3":
                input(f"\n{lista}")
            case "4":
                busqueda = lista.search(
                    input("\nIngrese el dato que desea buscar en la lista: ")
                )

                if busqueda is None:
                    input("\n¡Error! Dato ingresado no existe en la lista...")
                    continue

                input(f"\nElemento a modificar: {busqueda.data}")
                busqueda.data = input("\nIngrese el nuevo valor del elemento: ")
            case "5":
                busqueda = lista.search(
                    input("\nIngrese el dato que desea buscar en la lista: ")
                )

                if busqueda is None:
                    input("\n¡Error! Dato ingresado no existe en la lista...")
                    continue

                input(f"\nElemento eliminado: {busqueda.data}...")
                lista.delete(busqueda.data)
            case "6":
                print("\nSaliendo del programa...\n")
            case _:
                input("\n¡Opción inválida, intente nuevamente!")


def main() -> None:
    """
    Ejecución del programa.
    """

    menu()


if __name__ == "__main__":
    main()
