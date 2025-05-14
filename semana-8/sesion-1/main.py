"""
La fila de clientes entrando a un cine se puede manejar utilizando una cola.
"""

from os import system

from . import Cliente, Cola, SisCine


def menu_principal(sis: SisCine) -> None:
    """
    Loop principal del programa que le muestra un menú de opciones al usuario.
    """

    opcion = ""
    while opcion != "5":
        system("cls || clear")
        print("\nSistema de Entrada para Cines")
        print("-----------------------------------------------------\n")
        print("1. Agregar cliente a fila")
        print("2. Ver siguiente cliente")
        print("3. Atender siguiente cliente")
        print("4. Mostrar estado actual de la fila")
        print("5. Salir")

        opcion = input("\n-> ")

        match opcion:
            case "1":
                print("\nIngrese datos del cliente nuevo:")
                print("--------------------------------")
                sis.agregar_cliente(
                    Cliente(
                        input("ID del boleto del cliente: "),
                        input("Nombre del cliente: "),
                        input("Película que verá el cliente: "),
                    )
                )
            case "2":
                print(f"Próximo cliente en la fila:\n{sis.atender_cliente()}")
            case "3":
                print(f"Cliente atendido:\n{sis.atender_cliente()}")
            case "4":
                input(f"\nEstado actual de la fila:\n{str(sis)}")
            case "5":
                print("\nSaliendo del programa...\n")
            case _:
                input("\n¡Opción inválida, intente nuevamente!")


def main() -> None:
    """
    Ejecución del programa.
    """

    menu_principal(sis=SisCine(Cola()))


if __name__ == "__main__":
    main()
