"""
Control de ventas de los empleados (3) de una empresa
de electrodomesticos durante un trimestre.
"""

NUM_MESES = 3
NUM_EMPLEADOS = 3

tabla_ventas = []
tabla_empleados = []


for i in range(NUM_EMPLEADOS):
    nombre = input(f"\nIngrese el nombre del empleado #{i + 1}: ")
    tabla_empleados.append(nombre)


for j in range(NUM_EMPLEADOS):
    fila = []
    for k in range(NUM_MESES):
        fila.append(
            float(
                input(
                    f"\nIngrese la venta del empleado #{j + 1} para el mes #{k + 1}: "
                )
            )
        )

    tabla_ventas.append(fila)


print("\nEmpleados:\n", "\n".join(empleado for empleado in tabla_empleados))
print("\nVentas:\n", "\n".join(str(venta) for venta in tabla_ventas))

print("\nInformación de Ventas:\n")
print("Nombre\t\tMes #1\t\tMes #2\t\tMes #3")

for i, nombre in enumerate(tabla_empleados):
    print(
        f"{nombre}\t\t" +
        f"{tabla_ventas[i][0]:.1f}\t\t" +
        f"{tabla_ventas[i][1]:.1f}\t\t" +
        f"{tabla_ventas[i][2]:.1f}"
    )
