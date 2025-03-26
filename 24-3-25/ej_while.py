"""
Pedir la nota final de una asignatura para n estudiantes y determinar si
la calificación es menor a 70 (reprobado), entre 70 y 79 (regular),
entre 80 y 89 (bueno), o entre 90 y 100 (excelente).
"""


notas = []
num_estudiantes = int(input("\nIngrese el número de estudiantes: "))
print()


for i in range(num_estudiantes):
    notas.append(
        float(input(f"Ingrese la nota del estudiante #{i + 1}: "))
    )


print("\n")

j = 0
while j < len(notas):
    nota = notas[j]

    if nota < 0 or nota > 100:
        print(f"Nota #{j + 1}: inválida, debe tener un valor entre 0 y 100!")
    elif nota < 70:
        print(f"Nota #{j + 1}: reprobada!")
    elif nota < 80:
        print(f"Nota #{j + 1}: regular!")
    elif nota < 90:
        print(f"Nota #{j + 1}: buena!")
    elif nota < 100:
        print(f"Nota #{j + 1}: excelente!")

    j += 1

print()
