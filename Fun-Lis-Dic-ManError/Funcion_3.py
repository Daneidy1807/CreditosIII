print("este ejemplo 3")

def getEmpleado(nombre, cc = None):
    print("Empleado")
    print(f"Nombre: {nombre}" )

    if cc!=None:
        print(f"cc: {cc}")
getEmpleado("Andrea Mapallo", 1060240356)        
