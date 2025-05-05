"""
Se desea implementar el historial de acciones realizadas por un usuario en un
editor de texto (como escribir, borrar, pegar, copiar). Cada acción debe
guardarse en orden y poder recorrerlas en ambas direcciones,
simulando las acciones de Deshacer y Rehacer.
"""

from . import EditorTexto


def menu_principal():
    """
    Función para mostrar el menú principal.
    """

    print("\n=== EDITOR DE TEXTO ===")
    print("1. Escribir texto")
    print("2. Borrar texto")
    print("3. Copiar texto")
    print("4. Pegar texto")
    print("5. Deshacer")
    print("6. Rehacer")
    print("7. Mover cursor")
    print("8. Ver historial")
    print("9. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def main():
    """
    Ejecución del programa.
    """

    editor = EditorTexto()

    while True:
        editor.mostrar_estado()
        opcion = menu_principal()

        if opcion == "1":  # Escribir
            texto = input("Texto a escribir: ")
            editor.escribir(texto)

        elif opcion == "2":  # Borrar
            try:
                longitud = int(input("Número de caracteres a borrar: "))
                editor.borrar(longitud)
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opcion == "3":  # Copiar
            try:
                longitud = int(input("Número de caracteres a copiar: "))
                editor.copiar(longitud)
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opcion == "4":  # Pegar
            editor.pegar()

        elif opcion == "5":  # Deshacer
            if not editor.deshacer():
                print("No hay más acciones para deshacer.")

        elif opcion == "6":  # Rehacer
            if not editor.rehacer():
                print("No hay más acciones para rehacer.")

        elif opcion == "7":  # Mover cursor
            try:
                nueva_posicion = int(
                    input(f"Nueva posición del cursor (0-{len(editor.texto)}): ")
                )
                if 0 <= nueva_posicion <= len(editor.texto):
                    editor.posicion_cursor = nueva_posicion
                else:
                    print("Posición fuera de rango.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opcion == "8":  # Ver historial
            editor.mostrar_historial()

        elif opcion == "9":  # Salir
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
