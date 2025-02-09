class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def cumpleanos(self):
        self.edad += 1

    def __str__(self):
        return "Nombre: " + self.nombre + ", Edad: " + str(self.edad)
    
primerpersona = persona("Juan", 25)

print(primerpersona)

primerpersona.cumpleanos()

print(primerpersona) 


