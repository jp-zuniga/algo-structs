"""
Un estudiante universitario desea llevar el control de sus gastos mensuales
relacionados con sus estudios, como transporte, alimentación, materiales
educativos, conexión a internet, alquiler, entre otros.

Desarrolla una aplicación en Python que le permita al estudiante:
    1. Registrar sus categorías de gastos.
    2. Agregar múltiples gastos individuales, indicando:
        − Fecha (como cadena de texto)
        − Categoría (de las previamente registradas)
        − Monto del gasto
        − Descripción corta
    3. Mostrar el total gastado en el mes.
    4. Mostrar el total por cada categoría.
    5. Listar todos los gastos realizados.
    6. Mostrar el gasto promedio por categoría.
    7. El programa debe estar organizado utilizando:
        − Funciones/módulos propios (4)
        − Solamente una clase
        − Uso de listas para almacenar los gastos
        − Uso adecuado de estructuras de control (condicionales y bucles)
"""

from locale import LC_TIME, setlocale
from os import system

from control_gastos import (
    agregar_gasto,
    encontrar_total,
    Gasto,
    mostrar_gastos,
    promediar_categoria,
)


def menu_principal(gastos: list[Gasto]) -> None:
    """
    Loop principal del programa que le muestra un menú de opciones al usuario.
    """

    opcion = ""
    while opcion != "7":
        system("cls || clear")
        print("\nGestión de Gastos")
        print("-----------------------------------------------------\n")
        print("1. Agregar gasto")
        print("2. Registrar nueva categoría de gasto")
        print("3. Mostrar gastos de un mes")
        print("4. Mostrar gastos de una categoría")
        print("5. Calcular totales")
        print("6. Promediar gastos de categoría")
        print("7. Salir")

        opcion = input("\n-> ")

        match opcion:
            case "1":
                system("cls || clear")
                agregar_gasto(gastos)
            case "2":
                system("cls || clear")
                print("\nCategorías Registradas:")
                print("*****************************************************\n")

                for i, cat in enumerate(Gasto.categorias()):
                    print(f"{i + 1}. {cat}")

                print("\nIngrese la nueva categoría:")
                input(f"{len(Gasto.categorias()) + 1}. ")
            case "3":
                system("cls || clear")
                try:
                    mes = int(
                        input(
                            "\nIngrese el número del mes de gastos que desea visualizar: "
                        )
                    )
                    if mes <= 0 or mes > 12:
                        raise ValueError

                    mostrar_gastos(gastos, mes)
                except (TypeError, ValueError):
                    input("¡Error! Debe ingresar un número de mes válido (1-12).")
                    continue
            case "4":
                system("cls || clear")
                cat = input("\nIngrese la categoría de gastos que desea visualizar: ")
                if not Gasto.validar_categoria(cat):
                    input("¡Debe ingresar una categoría registrada!")
                    continue

                mostrar_gastos(gastos, cat)
            case "5":
                system("cls || clear")
                tipo = input(
                    "\n¿Desea encontrar el total de gastos de un mes (1)"
                    + " o de una categoría (2)? (1/2)"
                )

                if tipo == "1":
                    try:
                        mes = int(
                            input(
                                "\nIngrese el número del mes de gastos que desea visualizar: "
                            )
                        )
                        if mes <= 0 or mes > 12:
                            raise ValueError

                        encontrar_total(gastos, mes)
                    except (TypeError, ValueError):
                        input("¡Error! Debe ingresar un número de mes válido (1-12).")
                        continue
                elif tipo == "2":
                    cat = input("\nIngrese la categoría de gastos que desea visualizar: ")
                    if not Gasto.validar_categoria(cat):
                        input("¡Debe ingresar una categoría registrada!")
                        continue

                    encontrar_total(gastos, cat)
                else:
                    input("\n¡Error! Debe ingresar una respuesta inválida.")
            case "6":
                system("cls || clear")
                cat = input("\nIngrese la categoría de gastos que desea visualizar: ")
                if not Gasto.validar_categoria(cat):
                    input("¡Debe ingresar una categoría registrada!")
                    continue

                promediar_categoria(gastos, cat)
            case "7":
                print("\nSaliendo del programa...\n")
            case _:
                input("\n¡Opción inválida, intente nuevamente!")


def main() -> None:
    """
    Ejecución del programa.
    """

    gastos: list[Gasto] = []
    menu_principal(gastos)


if __name__ == "__main__":
    setlocale(LC_TIME, "es_ES")
    main()
