# Variable global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"
print(frase)
def holaMundo():
    frase = "Hola mundo!!"
    print("Dentro de la función:")
    print(frase)
    year = 2021
    print(year)
    global website
    website = "andreamelenje.com"
    print("DENTRO: ", website)
    return "Dato devuelto " + str(year)
print(holaMundo())
print("FUERA: ", website)