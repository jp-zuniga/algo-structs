"""
Control de ventas de los empleados (3) de una empresa
de electrodomesticos durante un trimestre.
"""

num_meses = 3
num_empleados = 3

tabla_ventas = []
tabla_empleados = []


for i in range(num_empleados):
    nombre = input(f"\nIngrese el nombre del empleado #{i + 1}: ")
    tabla_empleados.append(nombre)


for j in range(num_empleados):
    fila = []
    for k in range(num_meses):
        fila.append(float(
            input(
                f"\nIngrese la venta del empleado #{j + 1} para el mes #{k + 1}: "
            )
        ))

    tabla_ventas.append(fila)


print("\nEmpleados:\n", "\n".join(empleado for empleado in tabla_empleados))
print("\nVentas:\n", "\n".join(str(venta) for venta in tabla_ventas))

print("\nInformacion de Ventas:\n")
print("Nombre\t\tEnero\t\tFebrero\t\tMarzo")


for i, nombre in enumerate(tabla_empleados):
    print(
        f"{nombre}\t\t{tabla_ventas[i][0]:.1f}" +
        f"\t\t{tabla_ventas[i][1]:.1f}\t\t" +
        f"{tabla_ventas[i][2]:.1f}"
    )
