"""
Una clínica recibe pacientes en orden de llegada. Cada paciente debe ser ingresado al
sistema con los siguientes datos: nombre completo, edad, síntoma principal y prioridad
(de 1 a 5). El sistema debe permitir insertar nuevos pacientes, recorrer la lista
para mostrar el orden de atención, y eliminar a un paciente una vez atendido.
"""

from os import system

from . import LinkedList, Paciente


def agregar_paciente(lista: LinkedList[Paciente]) -> None:
    """
    Pide los datos del nuevo paciente y lo agrega a la lista.
    """

    print(f"\nPaciente {len(lista) + 1}:\n")

    try:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        if edad < 0:
            raise ValueError

        sintoma = input("Síntoma principal: ")
        prioridad = int(input("Prioridad (1-5): "))
        if prioridad < 1 or prioridad > 5:
            raise ValueError

    except (TypeError, ValueError):
        input(
            "\n¡Error! La edad debe ser mayor a cero, y la prioridad"
            + " debe ser un número entre 1 y 5, intente nuevamente..."
        )

        agregar_paciente(lista)

    lista.add_at_end(Paciente(
        nombre,
        edad,
        sintoma,
        prioridad
    ))


def consultar_pacientes(lista: LinkedList[Paciente]) -> None:
    """
    Muestra todos los pacientes en la lista, ordenados por su prioridad.
    """

    lista_filtrada: list[tuple[str, int]] = []

    current = lista.head
    while current is not None:
        lista_filtrada.append((current.data.nombre, current.data.prioridad))
        current = current.next

    # ordenar la lista de tuplas por el segundo elemento (el atributo del objeto)
    lista_filtrada.sort(key=lambda x: x[1])

    print()
    for i, paciente in enumerate(lista_filtrada):
        print(f"{i + 1}. Prioridad de {paciente[0]}: {paciente[1]}")
    print()


def eliminar_paciente(lista: LinkedList[Paciente]) -> None:
    """
    Pide el nombre del paciente a eliminar despues de ser atendido.
    """

    nombre = input("\nIngrese el nombre del paciente a eliminar: ")

    previous = None
    current = lista.head

    while current is not None:
        if current.data.nombre == nombre:
            if previous is None:
                lista.head = current.next
            else:
                previous.next = current.next
        previous = current
        current = current.next


def menu_principal(lista: LinkedList[Paciente]) -> None:
    """
    Loop principal del programa que le muestra un menú de opciones al usuario.
    """

    opcion = ""
    while opcion != "4":
        system("cls || clear")
        print("\nGestión de Pacientes")
        print("-----------------------------------------------------\n")
        print("1. Agregar paciente")
        print("2. Consultar pacientes")
        print("3. Eliminar paciente")
        print("4. Salir")

        opcion = input("\n-> ")

        match opcion:
            case "1":
                system("cls || clear")
                agregar_paciente(lista)
            case "2":
                system("cls || clear")
                consultar_pacientes(lista)
                input("\nPresione 'Enter' para regresar al menú principal...")
            case "3":
                system("cls || clear")
                eliminar_paciente(lista)
            case "4":
                print("\nSaliendo del programa...\n")
            case _:
                input("\n¡Opción inválida, intente nuevamente!")


def main() -> None:
    """
    Ejecución del programa.
    """

    menu_principal(LinkedList())


if __name__ == "__main__":
    main()
