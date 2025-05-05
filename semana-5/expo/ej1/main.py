"""
Una escuela de educación primaria requiere un algoritmo que muestre los datos de los
estudiantes de un salón de clase ordenados de forma ascendente, según un parámetro
indicado; este parámetro puede ser cualquiera de los siguientes campos:
carnet, nombres, apellidos, genero, peso, estatura, promedio.
"""

from typing import Union

from . import Estudiante, LinkedList


def input_estudiantes(lista: LinkedList[Estudiante]) -> None:
    """
    Guarda los datos de estudiantes ingresados en una lista enlazada.
    """

    i = 1

    while True:
        print("\nPara terminar, dejar todos los campos vacíos.\n")

        try:
            carnet = input(f"Ingrese el carnet del estudiante #{i}: ")
            nombres = input(f"Ingrese los nombres del estudiante #{i}: ")
            apellidos = input(f"Ingrese los apellidos del estudiante #{i}: ")
            genero = input(f"Ingrese el género del estudiante #{i}: ")

            peso = input(f"Ingrese el peso del estudiante #{i} (en kg): ")
            if peso != "" and float(peso) <= 0:
                raise ValueError

            estatura = input(f"Ingrese la estatura del estudiante #{i} (en m): ")
            if peso != "" and float(estatura) <= 0:
                raise ValueError

            promedio = input(f"Ingrese el promedio del estudiante #{i}: ")
            if peso != "" and float(promedio) <= 0:
                raise ValueError

        except (TypeError, ValueError):
            input(
                "\n¡Error! El peso, promedio y estatura del estudiante deben"
                + " ser un número real positivo, intente nuevamente..."
            )

            continue

        if all(
            x == ""
            for x in (carnet, nombres, apellidos, genero, peso, estatura, promedio)
        ):
            break

        i += 1
        lista.add_at_end(Estudiante(
            carnet=carnet,
            nombres=tuple(nombres.split()),
            apellidos=tuple(apellidos.split()),
            genero=genero,
            peso=float(peso),
            estatura=float(estatura),
            promedio=float(promedio)
        ))

    print()


def print_ordenado(lista: LinkedList[Estudiante], filtro: int) -> None:
    """
    Imprime los datos de la lista de estudiantes,
    ordenados ascendientemente según el filtro especificado.
    """

    lista_filtrada: list[tuple[str, Union[str, float]]] = []

    # hay que extraer los nombres de todos los estudiantes de la lista
    # y emparejarlos con el dato que se desea visualizar y ordenar

    current = lista.head
    while current is not None:
        # construir un string con el primer nombre y primer apellido
        key = f"{current.data.nombres[0]} {current.data.apellidos[0]}"

        # extraer el atributo correspondiente al filtro especificado
        match filtro:
            case 1:
                atributo = "Carnet"
                value = current.data.carnet
            case 2:
                atributo = "Nombres"
                value = current.data.nombres
            case 3:
                atributo = "Apellidos"
                value = current.data.apellidos
            case 4:
                atributo = "Género"
                value = current.data.genero
            case 5:
                atributo = "Peso"
                value = current.data.peso
            case 6:
                atributo = "Estatura"
                value = current.data.estatura
            case 7:
                atributo = "Promedio"
                value = current.data.promedio

        # guardar la entrada en la lista
        lista_filtrada.append((key, value))
        current = current.next

    # ordenar la lista de tuplas por el segundo elemento (el atributo del objeto)
    lista_filtrada.sort(key=lambda x: x[1])

    print()
    for i, estudiante in enumerate(lista_filtrada):
        print(f"{i + 1}. {atributo} de {estudiante[0]}: {estudiante[1]}")
    print()


def main() -> None:
    """
    Ejecución del programa.
    """

    lista: LinkedList[Estudiante] = LinkedList()
    print("\nPrimeramente, debe ingresar los datos de los estudiantes de la clase:")
    print("---------------------------------------------------------------------")

    input_estudiantes(lista)
    print("\nAhora, seleccione el campo por el cual desea ordenar los datos:")
    print("1. Carnet\n2. Nombres\n3. Apellidos\n4. Genero\n5. Peso\n6. Estatura\n7. Promedio")

    seleccion = input("=> ")

    if seleccion.isnumeric():
        print_ordenado(lista, int(seleccion))
    else:
        input("\n¡Error! No seleccionó una opción válida, intente nuevamente...\n")



if __name__ == "__main__":
    main()
