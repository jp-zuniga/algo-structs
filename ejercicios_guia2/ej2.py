"""
Desarrollar un programa que permita al usuario gestionar una cuenta bancaria.
El programa deberá utilizar un menú que permita realizar diferentes operaciones
sobre el saldo de la cuenta. El programa debe permitir al usuario ingresar la
cantidad para depositar o retirar, actualizar el saldo y mostrar los resultados.
Si se elige la opción de retiro, debe verificar que el saldo sea suficiente.
"""

from os import system


def consultar_saldo(saldo: float) -> None:
    """
    Muestra el saldo de la cuenta del usuario.
    """

    print("\nEstado de Cuenta:")
    print("---------------------------------------------")
    print(f"Saldo actual: {saldo:.2f}")
    input("\nPresione 'Enter' para regresar al menú principal...")


def pedir_monto(accion: str) -> float:
    """
    Le pide un monto al usuario para realizar
    una acción con su cuenta bancaria.
    """

    try:
        monto = float(input(f"\nIngrese el monto que desea {accion}: "))
        if monto <= 0:
            raise ValueError
    except (TypeError, ValueError):
        input("\n¡El monto debe ser un número real positivo!")
        return pedir_monto(accion)

    return monto


def depositar(saldo: float) -> float:
    """
    Deposita el monto deseado en la cuenta del usuario.
    """

    saldo += pedir_monto("depositar")
    input("\n¡Monto depositado exitosamente!")
    return saldo


def retirar(saldo: float) -> float:
    """
    Retira el monto deseado de la cuenta del usuario.
    """

    monto = pedir_monto("retirar")

    if monto > saldo:
        input(
            "\n¡Error! Monto ingresado es mayor que el saldo"
            + " actual, por favor intente nuevamente..."
        )
    else:
        saldo -= monto
        input("\n¡Monto retirado exitosamente!")

    return saldo


def menu_principal(saldo: float) -> None:
    """
    Loop principal del programa que le muestra un menú de opciones al usuario.
    """

    opcion = ""
    while opcion != "4":
        system("cls || clear")
        print("\nGestión de Cuenta Bancaria")
        print("-----------------------------------------------------\n")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")

        opcion = input("\n-> ")

        match opcion:
            case "1":
                system("cls || clear")
                consultar_saldo(saldo)
            case "2":
                saldo = depositar(saldo)
            case "3":
                saldo = retirar(saldo)
            case "4":
                print("\nSaliendo del programa...\n")
            case _:
                input("\n¡Opción inválida, intente nuevamente!")


def main() -> None:
    """
    Ejecución del programa.
    """

    saldo = 0.0
    menu_principal(saldo)


if __name__ == "__main__":
    main()
