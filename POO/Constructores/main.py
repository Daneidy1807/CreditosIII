from coche import coche

carro = coche("Amarillo", "Renault", "Clio", 150, 200,4)
carro1 = coche("Verde", "Seat", "Panda", 240, 200,4)
carro2 = coche("Azul", "Citroen", "Xara", 100, 180,4)
carro3 = coche("Rojo", "Mercedes", "Clase A", 350, 400,4)


print("este es el color de ", carro.getcolor())
print(carro.getInfo(), carro2.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())