"""
Módulo que implementa algoritmos de ordenamiento simples.
"""


def bubble_sort(lista):
    """
    Implementación del algoritmo Bubble Sort.
    Ordena una lista comparando elementos adyacentes y
    realizando intercambios hasta que la lista esté ordenada.
    """

    # Trabajamos con una copia para no modificar la original
    resultado = lista.copy()
    n = len(resultado)

    intercambio_realizado = True
    iteraciones = 0

    # Realizamos n - 1 pasadas como máximo
    for i in range(n - 1):
        # Si no hubo intercambios en la pasada anterior, la lista ya está ordenada
        if not intercambio_realizado:
            break

        intercambio_realizado = False
        iteraciones += 1

        # En cada pasada, comparamos elementos adyacentes
        for j in range(n - i - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if resultado[j] > resultado[j + 1]:
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
                intercambio_realizado = True

    return resultado, iteraciones


def print_paso_a_paso(lista):
    """
    Muestra la ejecución paso a paso del algoritmo bubble sort.
    """

    resultado = lista.copy()
    n = len(resultado)

    print("\nEstado inicial: ", resultado)

    # Seguimiento de pasos
    paso = 1

    for i in range(n - 1):
        hubo_cambios = False

        print(f"\nPasada #{i + 1}:")

        for j in range(n - i - 1):
            print(f" -> Paso #{paso}: Comparando {resultado[j]} y {resultado[j + 1]}")

            if resultado[j] > resultado[j + 1]:
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
                print(f"Intercambio: {resultado}")
                hubo_cambios = True
            else:
                print(f"Sin cambios: {resultado}")

            paso += 1

        if not hubo_cambios:
            print("  No se realizaron intercambios. Lista ordenada.")
            break

    return resultado
