num=1
aprobado=0
reprobado=0

while num<10:
    numero=int(input(f"Ingrese nota del estudiante {num} ingrese nota: "))
    if numero>=3:
        aprobado +=1
    else:
        reprobado +=1
    num +=1
print(f"Estudiantes aprobados {aprobado}")    
print(f"Estudiantes reprobados {reprobado}")