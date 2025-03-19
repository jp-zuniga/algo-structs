"""
Calcular los salarios semanales de los empleados de una empresa, sabiendo que
estos se calculan en base a las horas semanales trabajadas y de acuerdo a un precio
especificado por cada hora. Si se pasan de 48 horas semenales, las horas
extraodrinarias se pagarán a razón de dos veces la hora ordinaria.
"""


empleados = {}
num_empleados = int(input("¿Cuántos empleados hay en su empresa? "))
salario = float(input("¿Cuánto se le paga a los empleados por hora? "))

print()

for i in range(num_empleados):
    nombre = input(f"¿Cuál es el nombre del empleado #{i + 1}? ")
    horas = int(input(f"¿Cuántas horas trabajo {nombre}? "))

    empleados[nombre] = horas
    print()

print()

for nombre, horas in empleados.items():
    if horas <= 48:
        print(f"{nombre}: C${salario * horas}")
    else:
        horas_extra = horas - 48
        pago = (salario * (horas - horas_extra)) + (2 * salario * horas_extra)
        print(f"{nombre}: C${pago}")
