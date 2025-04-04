"""
Ejemplo de paquetes y módulos.
"""

from empleado import Empleado  # pylint: disable=E0401


def main() -> None:
    """
    Ejecución del programa.
    """

    empleados = []
    n = int(input("\nIngrese la cantidad de empleados: "))

    print("\nIngrese los datos de los empleados:")
    for _ in range(n):
        nombre = input("Nombre: ")
        salario_bruto = float(input("Salario Bruto: "))
        empleados.append(Empleado(nombre, salario_bruto))

    print("\nDatos del Empleado:\n")
    for emp in empleados:
        print(emp.nombre)
        print(emp.calcular_salario_neto())


if __name__ == "__main__":
    main()
