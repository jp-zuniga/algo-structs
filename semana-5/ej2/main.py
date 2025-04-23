"""
Se requiere automatizar un mapa que contiene las estaciones de una
ruta previamente establecida para una aplicación que indique, a
partir de un punto de la ruta, el tiempo estimado para llegar
a un destino determinado de la misma.
"""

from . import Ruta


def main():
    """
    Ejecución del programa.
    """

    # Crear el mapa de la ruta
    mapa = Ruta()

    while True:
        print("\n=== SISTEMA DE CÁLCULO DE TIEMPO DE VIAJE ===")
        print("1. Ver estaciones disponibles")
        print("2. Agregar nueva estación")
        print("3. Conectar estaciones")
        print("4. Ver todas las conexiones")
        print("5. Calcular tiempo de viaje")
        print("6. Salir")

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            estaciones = mapa.mostrar_estaciones()
            print("\nEstaciones disponibles:")
            for i, estacion in enumerate(estaciones, 1):
                print(f"{i}. {estacion}")

        elif opcion == "2":
            nombre = input("Ingrese el nombre de la nueva estación: ")
            if mapa.agregar_estacion(nombre):
                print(f"Estación '{nombre}' agregada correctamente.")
            else:
                print(f"La estación '{nombre}' ya existe.")

        elif opcion == "3":
            estaciones = mapa.mostrar_estaciones()
            print("\nEstaciones disponibles:")
            for i, estacion in enumerate(estaciones, 1):
                print(f"{i}. {estacion}")

            try:
                idx_origen = (
                    int(input("\nSeleccione el número de la estación de origen: ")) - 1
                )

                idx_destino = (
                    int(input("Seleccione el número de la estación de destino: ")) - 1
                )

                tiempo = int(
                    input("Ingrese el tiempo en minutos entre las estaciones: ")
                )

                if (
                    0 <= idx_origen < len(estaciones)
                    and
                    0 <= idx_destino < len(estaciones)
                ):
                    origen = estaciones[idx_origen]
                    destino = estaciones[idx_destino]

                    if mapa.conectar_estaciones(origen, destino, tiempo):
                        print(
                            f"Conexión de {origen} a {destino} ({tiempo} minutos) establecida."
                        )
                    else:
                        print("No se pudo establecer la conexión.")
                else:
                    print("Selección de estación inválida.")
            except ValueError:
                print("Entrada inválida. Ingrese números válidos.")

        elif opcion == "4":
            conexiones = mapa.obtener_conexiones()
            print("\nConexiones actuales:")
            for i, (origen, destino, tiempo) in enumerate(conexiones, 1):
                print(f"{i}. {origen} → {destino}: {tiempo} minutos")

        elif opcion == "5":
            estaciones = mapa.mostrar_estaciones()
            print("\nEstaciones disponibles:")
            for i, estacion in enumerate(estaciones, 1):
                print(f"{i}. {estacion}")

            try:
                idx_inicio = (
                    int(input("\nSeleccione el número de la estación de inicio: ")) - 1
                )

                idx_fin = (
                    int(input("Seleccione el número de la estación de destino: ")) - 1
                )

                if 0 <= idx_inicio < len(estaciones) and 0 <= idx_fin < len(estaciones):
                    inicio = estaciones[idx_inicio]
                    fin = estaciones[idx_fin]

                    ruta, tiempo_total = mapa.calcular_ruta_mas_rapida(inicio, fin)

                    if ruta:
                        print(f"\nRuta más rápida de {inicio} a {fin}:")
                        print(" → ".join(ruta))
                        print(f"Tiempo total estimado: {tiempo_total} minutos")
                    else:
                        print(f"No se encontró una ruta de {inicio} a {fin}.")
                else:
                    print("Selección de estación inválida.")
            except ValueError:
                print("Entrada inválida. Ingrese números válidos.")

        elif opcion == "6":
            print("¡Gracias por usar el sistema de cálculo de tiempo de viaje!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 6.")


if __name__ == "__main__":
    main()
