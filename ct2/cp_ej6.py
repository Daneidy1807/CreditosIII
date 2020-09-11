#diccionario
#ingresa un dato y lo cambia
datos=[
    {
        'nombre':'andrea',
        'correo':'andrea@gmail.com',
        'carrera':'sistemas'
    },
    {
        'nombre':'daneidy',
        'correo':'daneidy@gmail.com',
        'carrera':'psicologia'
    }
]

if datos:
    indice=int(input('Ingrese posicion a modificar en el diccionario '))

    if indice<datos.__len__():
        subIndice=int(input('seleccionar opcion del 1 al 3 \n 1 nombre \n 2 correo \n 3 carrera \n'))
        if(subIndice<datos[indice].__len__()):
            cambio=input('ingrese cambio  ')
            if subIndice==1:
                datos[indice]['nombre']=cambio
            elif subIndice==2:
                datos[indice]['correo']=cambio
            elif subIndice==3:
                datos[indice]['carrera']=cambio
        else:
            print('este subIndice no existe')
    else:
        print('este indice no existe en el dicionario')   
else:
    print('el diccionario no existe o esta vacio')


#print(datos)
for dato in datos:
    print(f"Nombre : {dato['nombre']}")
    print(f"Correo : {dato['correo']}")
    print(f"Carrera : {dato['carrera']}")