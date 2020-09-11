#3 variables y un mensaje diciendo el tipo de dato con funciones
n1='ole'
n2=True
n3=[1,2,3]
n4=1
#print(type(n4))
def tipoDato(variable):
    if type(variable) is str:
        print('tipo de dato string')
    elif type(variable) is bool:
        print('tipo de dato booleano')
    elif type(variable) is list:
        print('tipo de dato lista')
    elif type(variable) is int:
        print('tipo de dato int')

tipoDato(n1)
tipoDato(n2)
tipoDato(n3)
tipoDato(n4)