print("####### EJEMPLO 3 #######")
# Parametros opcionales
def getEmpleado(nombre, cc = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if cc != None:
       print(f"cc: {cc}")
getEmpleado("andrea ", 488283)