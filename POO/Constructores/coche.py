class coche:
    #atributos
    color= "rojo"
    marca= "ferrari"
    modelo= "aventador"
    velocidad= 300
    caballaje= 500
    asientos=2
    
    #constructor
    def __init__(self, color, marca, modelo, velocidad,caballaje, plazas):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.color=color

    #metodos de la clase coche
    #def getPrivado(self)  
       # return self.__soy_privado

    def setcolor(self, color):
        self.color = color  

    def getcolor(self):
        return self.color 

    def setmodelo(self, modelo):
        self.modelo = modelo  

    def getmodelo(self):
        return self.modelo 

    def setmarca(self, marca):
        self.marca = marca 

    def getmarca(self):
        return self.marca           

    def acelerar(self):
        self.velocidad +=1

    def frenar(self):
        self.velocidad -=1

    def getvelocidad (self):
        return self.velocidad

    #metodo para acceder a toda la informacion del objeto
    def getInfo(self):
        info="----Informacion del coche ---" 
        info+= "\n Color: " + self.getcolor()
        info+= "\n Marca: " + self.getmarca()
        info+= "\n Modelo: " + self.getmodelo()  
        info+= "\n Velocidad: " + str(self.getvelocidad())
        return info 