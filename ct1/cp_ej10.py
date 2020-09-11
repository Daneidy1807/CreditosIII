#que estudiantes aprobaron y reprobaron 
aprobados=0
suspendidos=0

for alumnos in range(1,16):
    nota= int(input(f"ingrese nota del alumno {alumnos} : "))
    if nota >=3:
        aprobados+=1
    else:
        suspendidos+=1

print(f"alumnos aprobados {aprobados}")
print(f"alumnos suspendidos {suspendidos}")