class Casa:
    #atributos
    habitaciones = 4
    baños = 2
    garajes= 1
    cocinas= 1
    pisos= 2

    def __init__(self, habitaciones, baños, garajes, cocinas,pisos):
        self.habitaciones=habitaciones
        self.baños=baños
        self.garajes=garajes
        self.cocinas=cocinas
        self.pisos=pisos
        
    def getInfo(self):
        info="----Informacion del coche ---" 
        info+= "\n Habitaciones: " + str(self.habitaciones)
        info+= "\n Baños: " + str(self.baños)
        info+= "\n Garajes: " + str(self.garajes)  
        info+= "\n Cocinas: " + str(self.cocinas)
        info+= "\n Pisos: " + str(self.pisos)
        return info     
    