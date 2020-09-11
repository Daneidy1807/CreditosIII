class coche:

    color= "rojo"
    marca= "ferrari"
    modelo= "aventador"
    velocidad= 300
    caballos_f= 500
    asientos=2

        def setcolor(self, color):
             self.color = color   

          def acelerar(self):
             self.velocidad +=1

          def frenar(self):
             self.velocidad -=1

          def getvelocidad (self):
             return self.velocidad

coche1 = coche()#primer objeto
coche1.setcolor("amarillo")
print("la velocidad del coche1 es: ", coche1.velocidad)
print("el color del coche1 es: ", coche1.color)
print("el coche1 tiene: ", coche1.asientos, "asientos")

coche2 = coche()
#marca renult color=verde, velocidad=200,

coche2.color("verde")
coche2.marca("renult")
coche2.velocidad(200)


#coche1.getvelocidad()
#print(coche1.getvelocidad())
#print("la velocidad del coche es: ", coche.velocidad)
#print("")