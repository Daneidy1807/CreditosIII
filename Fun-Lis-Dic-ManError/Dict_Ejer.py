datos =[
    {
        'nombre':'',
        'cedula': '',
        'carrera':''
    }
]
datos[0]['nombre']= input("Ingrse el nombre: ")
datos[0]['cedula']= input("Ingrse la cedula: ")
datos[0]['carrera']= input("Ingrse la carrera: ")

for dato in datos:
    print(f"Nombre : {dato['nombre']}")
    print(f"Cedula : {dato['cedula']}")
    print(f"Carrera : {dato['carrera']}")