"""
Definición de la clase Empleado.
"""

from salario_neto import salario_neto  # pylint: disable=E0401


class Empleado:
    """
    Representa un empleado y permite acceder sus datos.
    """

    def __init__(self, nombre: str, salario_bruto: float):
        self.__nombre = nombre
        self.__salario_bruto = salario_bruto

    @property
    def nombre(self) -> str:
        """
        Getter para el atributo protegido __nombre.
        """

        return self.__nombre

    @property
    def salario_bruto(self) -> float:
        """
        Getter para el atributo protegido __salario_bruto.
        """

        return self.__salario_bruto

    def calcular_salario_neto(self) -> float:
        """
        Llama a la función salario_neto() con self.salario_bruto.
        """

        return salario_neto(self.salario_bruto)
