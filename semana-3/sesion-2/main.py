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
        emp = Empleado(nombre, salario_bruto)
        empleados.append(emp)

    print("\nDatos del Empleado:\n")
    for emp in empleados:
        print(emp.get_nombre())
        print(emp.get_salario_neto())


if __name__ == "__main__":
    main()
