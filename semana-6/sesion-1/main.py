"""
Utilice una pila para almacenar las páginas visitadas. Realizar las siguientes operaciones:
-> Visitar nueva página: agrega la página actual a la pila y cambia a la nueva página.
-> Retroceder (Atrás): extrae la última página de la pila y la muestra como la página actual.
-> Mostrar página actual: imprime la página en la que el usuario se encuentra.
"""

from os import system

from . import Pila, SimWeb


def menu_principal(sim: SimWeb) -> None:
    """
    Loop principal del programa que le muestra un menú de opciones al usuario.
    """

    opcion = ""
    while opcion != "4":
        system("cls || clear")
        print("\nSimulación de Navegación Web")
        print("-----------------------------------------------------\n")
        print("1. Visitar nueva página")
        print("2. Retroceder a página anterior")
        print("3. Mostrar página actual")
        print("4. Salir")

        opcion = input("\n-> ")

        match opcion:
            case "1":
                sim.visitar_nueva(input("\nIngrese la página que desea visitar: "))
                input(f"\nPágina actual: {sim.obtener_actual()}")
            case "2":
                sim.retroceder()
                input(f"\nPágina actual: {sim.obtener_actual()}")
            case "3":
                input(f"\nPágina actual: {sim.obtener_actual()}")
            case "4":
                print("\nSaliendo del programa...\n")
            case _:
                input("\n¡Opción inválida, intente nuevamente!")


def main() -> None:
    """
    Ejecución del programa.
    """

    menu_principal(SimWeb(paginas=Pila()))


if __name__ == "__main__":
    main()
