"""
Diseñar una clase Producto que incluya atributos como código, nombre, precio y
cantidad en stock. Además, los estudiantes deberán implementar una clase
Inventario que administre una colección de objetos Producto, incorporando
métodos para agregar, buscar, actualizar y eliminar productos.
"""

from os import system

from inventario import Inventario  # pylint: disable=E0401


def menu_principal(inventario: Inventario) -> None:
    """
    Loop principal del programa que le muestra un menú de opciones al usuario.
    """

    opcion = ""
    while opcion != "6":
        system("cls || clear")
        print("\nGestión de Inventario")
        print("-----------------------------------------------------\n")
        print("1. Agregar producto")
        print("2. Consultar un producto específico")
        print("3. Mostrar todos productos registrados")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("\n-> ")

        match opcion:
            case "1":
                system("cls || clear")
                inventario.agregar_producto()
            case "2":
                system("cls || clear")
                inventario.consultar_producto()
                input("\nPresione 'Enter' para regresar al menú principal...")
            case "3":
                system("cls || clear")
                inventario.mostrar_productos()
            case "4":
                system("cls || clear")
                inventario.modificar_producto()
            case "5":
                system("cls || clear")
                inventario.eliminar_producto()
            case "6":
                print("\nSaliendo del programa...\n")
            case _:
                input("\n¡Opción inválida, intente nuevamente!")
        inventario.productos.sort(key=lambda p: p.codigo)

def main() -> None:
    """
    Ejecución del programa.
    """

    menu_principal(Inventario())


if __name__ == "__main__":
    main()
