"""
Definición de la clase Empleado.
"""

from salario_neto import salario_neto  # pylint: disable=E0401


class Empleado:
    def __init__(self, nombre, salario_bruto):
        self.__nombre = nombre
        self.__salario_bruto = salario_bruto

    def get_nombre(self):
        print(self.__nombre)

    def get_salario_neto(self):
        return salario_neto(self.__salario_bruto)
