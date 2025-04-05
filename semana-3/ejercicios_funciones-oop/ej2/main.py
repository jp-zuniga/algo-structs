"""
Se requiere que los estudiantes diseñen un módulo independiente que
contenga implementaciones de algoritmos de ordenamiento simples (bubble sort).
A partir de una función principal, se deben invocar los métodos del
módulo para ordenar una lista de números.
"""

from os import system
from random import randint

from ordenamiento import bubble_sort, print_paso_a_paso


def ingresar_lista():
    """
    Permite al usuario ingresar una lista de números.
    """

    lista = []
    print("\nIngrese los números de la lista (deje en blanco para terminar):")

    while True:
        entrada = input("Número (o 'Enter' para terminar): ")
        if entrada == "":
            break

        try:
            numero = float(entrada)
            lista.append(numero)
        except ValueError:
            print("\nError: Ingrese un número válido.\n")

    return lista


def generar_lista_aleatoria():
    """
    Genera una lista de números aleatorios.
    """

    try:
        cantidad = int(input("\n¿Cuántos números desea generar? "))
        minimo = int(input("Valor mínimo: "))
        maximo = int(input("Valor máximo: "))

        if cantidad <= 0:
            input("\nError: La cantidad debe ser mayor a cero.")
            system("cls || clear")
            return generar_lista_aleatoria()

        if minimo > maximo:
            minimo, maximo = maximo, minimo

        return [randint(minimo, maximo) for _ in range(cantidad)]
    except ValueError:
        input("Error: Ingrese valores numéricos válidos.")
        return generar_lista_aleatoria()


def mostrar_menu():
    """
    Muestra el menú principal.
    """

    print("\n=== PROGRAMA DE ORDENAMIENTO ===")
    print("1. Ingresar lista manualmente")
    print("2. Generar lista aleatoria")
    print("3. Salir")

    return input("\nSeleccione una opción: ")


def main():
    """
    Función principal del programa.
    """

    lista = []

    while True:
        system("cls || clear")
        opcion = mostrar_menu()

        if opcion == "1":
            system("cls || clear")
            print("=== INGRESO MANUAL DE DATOS ===")
            lista = ingresar_lista()
        elif opcion == "2":
            system("cls || clear")
            print("=== GENERACIÓN DE LISTA ALEATORIA ===")
            lista = generar_lista_aleatoria()
            input(
                "\nLista generada exitosamente. Presione 'Enter' para ordenar la lista generada."
            )
        elif opcion == "3":
            input("\n¡Gracias por utilizar el programa de ordenamiento!")
            print()
            break
        else:
            input("\nOpción inválida. Intente nuevamente.")
            continue

        if not lista:
            input("\nNo hay datos para ordenar.")
            continue

        system("cls || clear")
        print("=== RESULTADOS DE ORDENAMIENTO ===")
        print("\nLista original:", lista)

        # Usamos el módulo de ordenamiento
        lista_ordenada, iteraciones = bubble_sort(lista)

        print("\nLista ordenada: ", lista_ordenada)
        print(f"\nOrdenamiento completado en {iteraciones} iteraciones.")

        ver_pasos = input("\n¿Desea ver el ordenamiento paso a paso? (s/n): ").lower()
        if ver_pasos == "s":
            system("cls || clear")
            print("=== ORDENAMIENTO PASO A PASO ===")
            print_paso_a_paso(lista)

        input("\nPresione 'Enter' para regresar al menú...")


if __name__ == "__main__":
    main()
