"""
Desarrollar un programa que se comporte como un diccionario Inglés-Español;
esto es, solicitará una palabra en inglés y escribirá la correspondiente
palabra en español. Para hacer más sencillo el ejercicio, el número de
parejas de palabras estará limitado a 5. Una vez finalizada la introducción
de las listas de palabras, pasamos al modo traducción, de forma que si
introducimos "green", la respuesta ha de ser "verde". Si la palabra
no se encuentra, se emitirá un mensaje que lo indique.
"""

from os import system


def crear_diccionario(diccionario: dict[str, str], limite: int = 5) -> dict[str, str]:
    """
    Crea un diccionario de palabras en inglés
    asociadas con su traducción al español.
    """

    if len(diccionario.keys()) == limite:
        return diccionario

    try:
        num_palabras = int(
            input("\n¿Cuántas palabras desea ingresar al diccionario? (máx. 5) ")
        )

        if num_palabras > 5:
            raise ValueError
    except (TypeError, ValueError):
        input(
            "\n¡Error! El tamaño máximo del diccionario es de 5 palabras;"
            + " por favor intente nuevamente..."
        )

        return diccionario

    for _ in range(num_palabras):
        diccionario[
            input("\nIngrese la palabra en inglés: ")
        ] = input(
            "\nIngrese la traducción de su palabra en español: "
        )

    return diccionario


def traducir(diccionario: dict[str, str]) -> None:
    """
    Pide una palabra e imprime su traducción a la pantalla.
    """

    palabra = input("\nIngrese la palabra (en inglés) que desea traducir: ")
    if palabra not in diccionario.keys():
        input(
            "\n¡Error! La palabra ingresada no se encuentra en el diccionario;"
            + " por favor intente nuevamente..."
        )
    else:
        print(f"\nInglés: {palabra}\nEspañol: {diccionario[palabra]}")
        input("\nPresione 'Enter' para regresar al menú principal...")

def menu_principal(diccionario: dict[str, str], limite: int = 5) -> None:
    """
    Loop principal del programa que le muestra un menú de opciones al usuario.
    """

    opcion = ""
    while opcion != "6":
        system("cls || clear")
        print("\nDiccionario Inglés-Español:")
        print("-----------------------------------------------------\n")
        print("1. Introducir palabras")
        print("2. Traducir")
        print("3. Salir")

        opcion = input("\n-> ")

        match opcion:
            case "1":
                system("cls || clear")
                crear_diccionario(diccionario, limite)
            case "2":
                system("cls || clear")
                traducir(diccionario)
            case "3":
                print("\nSaliendo del programa...\n")
            case _:
                input("\n¡Opción inválida, intente nuevamente!")


def main() -> None:
    """
    Ejecución del programa.
    """

    limite_palabras = 5
    diccionario: dict[str, str] = {}

    menu_principal(diccionario, limite_palabras)


if __name__ == "__main__":
    main()
