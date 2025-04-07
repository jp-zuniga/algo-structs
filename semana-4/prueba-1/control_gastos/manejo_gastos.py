"""
Implementaciones de funciones que permiten manejar
los gastos registrados en la aplicación.
"""

from datetime import date
from os import system
from typing import Union

from . import Gasto


def agregar_gasto(gastos: list[Gasto]) -> None:
    """
    Pide los datos de un producto nuevo y lo agrega a productos.
    """

    print("\nAgregar Gasto Nuevo:")
    print("*****************************************************")

    print("\nIngrese los detalles del gasto:")
    try:
        input_fecha = input("Fecha (en formato yyyy-mm-dd, o vacío para fecha actual): ")
        if input_fecha == "":
            fecha = date.today()
        else:
            fecha = date.fromisoformat(input_fecha)

        cat = input("Categoría: ")
        if not Gasto.validar_categoria(cat):
            raise ValueError("¡Debe ingresar una categoría registrada!")

        monto = float(input("Monto: C$"))
        if monto <= 0:
            raise ValueError("¡El precio debe ser un número real positivo!")

        desc = input("Descripción: ")

    except (TypeError, ValueError) as e:
        if "isoformat" not in str(e) or isinstance(e, TypeError):
            input(f"\n{e}")
        else:
            input("\n¡Error! La fecha debe ser ingresada en el formato yyyy-dd-mm.")

        system("cls || clear")
        return agregar_gasto(gastos)

    gastos.append(Gasto(len(gastos) - 1, fecha, cat, monto, desc))
    input("\n¡Gasto agregado exitosamente!")
    return None


def mostrar_gastos(gastos: list[Gasto], filtro: Union[int, str, None] = None) -> None:
    """
    Muestra los gastos que coinciden con el filtro de
    mes o categoría (None para mostrar todos los gastos).
    """

    if filtro is None:
        tipo = "Registrados"
        gastos_filtrados = gastos
    elif isinstance(filtro, int):
        if filtro <= 0 or filtro > 12:
            input("¡Error! Debe ingresar un número de mes válido (1-12).")
            return

        tipo = f"de {date(2025, filtro, 1).strftime("%B")}"
        gastos_filtrados = [g for g in gastos if g.fecha.month == filtro]
    else:
        if not Gasto.validar_categoria(filtro):
            input("¡Debe ingresar una categoría registrada!")
            return

        tipo = f"de {filtro}"
        gastos_filtrados = [g for g in gastos if g.categoria == filtro]

    print(f"\nGastos {tipo}:")
    print("*****************************************************")

    for i, gasto in enumerate(gastos_filtrados):
        print(f"\nGasto #{i + 1}:")
        print("---------------------------------------------")
        print(f"Fecha: {gasto.fecha}")
        print(f"Categoría: {gasto.categoria}")
        print(f"Monto: C${gasto.monto}")
        print(f"Descripción: {gasto.descripcion}")
        print("---------------------------------------------")

    input("\nPresione 'Enter' para regresar al menú principal...")


def encontrar_total(gastos: list[Gasto], filtro: Union[int, str, None] = None) -> None:
    """
    Encuentra el total de los gastos filtrados:
    -> si filtro es un int, encuentra el total de gastos del mes que corresponde al int
    -> si filtro es un str, encuentra el total de gastos de la categoría que corresponde
    -> si filtro es None, encuentra el total de todos los gastos registrados.
    """

    if filtro is None:
        tipo_gasto = "todos los gastos registrados"
        gastos_filtrados = gastos
    elif isinstance(filtro, int):
        tipo_gasto = f"todos los gastos de de {date(2025, filtro, 1).strftime("%B")}"
        gastos_filtrados = [g for g in gastos if g.fecha.month == filtro]
    else:
        tipo_gasto = f"de todos los gastos de {filtro}"
        gastos_filtrados = [g for g in gastos if g.categoria == filtro]

    total = sum(g.monto for g in gastos_filtrados)
    print(f"\nTotal de {tipo_gasto}: C$ {total}")
    input("\nPresione 'Enter' para regresar al menú principal...")


def promediar_categoria(gastos: list[Gasto], cat: str) -> None:
    """
    Encuentra el promedio de los gastos registrados en la categoría dada.
    """

    promedio = sum(g.monto for g in gastos if g.categoria == cat) / len(gastos)
    print(f"\nPromedio de todos los gastos de {cat}: C$ {promedio}")
    input("\nPresione 'Enter' para regresar al menú principal...")
