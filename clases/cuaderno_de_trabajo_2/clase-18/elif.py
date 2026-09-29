# elif permite evaluar otra condición cuando la anterior no se cumple

nota = 5.5

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprobado")
elif nota >= 5:
    print("Insuficiencia")
else:
    print("Reprobado")