"""
Desarrollar un programa que cargue los datos de un triángulo.
Implementar un método/función para determinar el tipo
de triángulo (equilátero, isósceles o escaleno).
"""


def main() -> None:
    """
    Ejecución del programa.
    """

    tipo = ""
    triangulo: list[float] = []

    for i in range(3):
        triangulo.append(float(input(f"Ingrese la longitud del lado #{i + 1}: ")))

    if triangulo[0] == triangulo[1] == triangulo[3]:
        tipo = "equilátero"
    elif (
        triangulo[0] == triangulo[1] or
        triangulo[1] == triangulo[2] or
        triangulo[0] == triangulo[2]
    ):
        tipo = "isósceles"
    else:
        tipo = "escaleno"

    print(f"\nEl triángulo ingresado es {tipo}.\n")


if __name__ == "__main__":
    main()
