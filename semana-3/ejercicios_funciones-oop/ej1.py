"""
Desarrollar un programa que procese un conjunto de registros de ventas
(por ejemplo, listas de diccionarios) para extraer información relevante.
Los estudiantes deberán aplicar funciones internas como map, filter y reduce
para transformar y filtrar los datos, calculando totales y promedios.
"""

from functools import reduce


def ingresar_ventas():
    """
    Permite al usuario ingresar registros de ventas.
    """

    ventas = []

    print("\n=== INGRESO DE DATOS DE VENTAS ===")
    print("(Dejar el producto en blanco para terminar)")

    while True:
        producto = input("\nProducto: ")
        if not producto:
            break

        try:
            precio = float(input("Precio: $"))
            cantidad = int(input("Cantidad: "))
            vendedor = input("Vendedor: ")

            ventas.append(
                {
                    "producto": producto,
                    "precio": precio,
                    "cantidad": cantidad,
                    "vendedor": vendedor,
                }
            )
        except ValueError:
            print("\nError: Ingrese valores numéricos válidos.\n")

    return ventas


def analizar_ventas(ventas):
    """
    Analiza los datos de ventas usando map, filter y reduce.
    """

    # Calcular subtotales con map
    subtotales = list(map(lambda v: v["precio"] * v["cantidad"], ventas))

    # Calcular total con reduce
    total = reduce(lambda x, y: x + y, subtotales, 0)

    # Calcular ventas por vendedor con filter y map
    vendedores = set(map(lambda v: v["vendedor"], ventas))
    ventas_por_vendedor = {}

    for vendedor in vendedores:
        ventas_vendedor = list(filter(lambda v: v["vendedor"] == vendedor, ventas))  # pylint: disable=W0640
        ventas_por_vendedor[vendedor] = sum(
            map(lambda v: v["precio"] * v["cantidad"], ventas_vendedor)
        )

    return subtotales, total, ventas_por_vendedor


def main():
    """
    Ejecución del programa.
    """

    # Ingreso de datos
    ventas = ingresar_ventas()

    if not ventas:
        print("\nNo se ingresaron datos para analizar.")
        return

    # Análisis de datos
    subtotales, total, ventas_por_vendedor = analizar_ventas(ventas)

    # Mostrar resultados
    print("\n=== RESULTADOS DEL ANÁLISIS ===")

    print("\n1. Registros ingresados:")
    for i, v in enumerate(ventas, 1):
        print(
            f"   {i}. {v['producto']}: ${v['precio']} x {v['cantidad']}" +
            f" - Vendedor: {v['vendedor']}"
        )

    print("\n2. Subtotales por venta:")
    for i, (v, subtotal) in enumerate(zip(ventas, subtotales), 1):
        print(f"   {i}. {v['producto']}: ${subtotal:.2f}")

    print(f"\n3. Total de ventas: ${total:.2f}")

    print("\n4. Ventas por vendedor:")
    for vendedor, monto in ventas_por_vendedor.items():
        print(f"   - {vendedor}: ${monto:.2f}")


if __name__ == "__main__":
    main()
