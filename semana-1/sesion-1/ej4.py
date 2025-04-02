"""
Pedir la nota final de una asignatura para n estudiantes y determinar si
la calificación es menor a 60 (reprobado), entre 60 y 69 (regular), entre
70 y 79 (bueno), entre 80 y 89 (muy bueno), o entre 90 y 100 (excelente).
"""

notas = []
num_estudiantes = int(input("\nIngrese el número de estudiantes: "))
print()


for i in range(num_estudiantes):
    notas.append(float(input(f"Ingrese la nota del estudiante #{i + 1}: ")))


print("\n")

for j, nota in enumerate(notas):
    if nota < 0 or nota > 100:
        print(f"Nota #{j + 1}: inválida, debe tener un valor entre 0 y 100!")
    elif nota < 60:
        print(f"Nota #{j + 1}: reprobada!")
    elif nota < 70:
        print(f"Nota #{j + 1}: regular!")
    elif nota < 80:
        print(f"Nota #{j + 1}: buena!")
    elif nota < 90:
        print(f"Nota #{j + 1}: muy buena!")
    elif nota < 100:
        print(f"Nota #{j + 1}: excelente!")

print()
