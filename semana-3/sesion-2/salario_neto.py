"""
Definición de la función salario_neto()
"""

def salario_neto(salario_bruto: float) -> float:
    """
    Calcula el salario neto de un empleado.
    """

    inss = salario_bruto * 0.07
    ir = (salario_bruto - inss) * 0.15

    return salario_bruto - inss - ir
