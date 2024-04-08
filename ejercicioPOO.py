class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self):
        return f"{self.nombre} fuerza= {self.fuerza} velocidad= {self.velocidad}"

    def __add__(self,otro):
        nuevo_nombre = self.nombre + "-" + otro.nombre
        nuevo_fuerza = ((self.fuerza + otro.fuerza)/2)**2
        nueva_velocidad = ((self.velocidad + otro.velocidad)/2)**2
        return Personaje(nuevo_nombre, nuevo_fuerza, nueva_velocidad)

goku = Personaje("Goku",100,100)
vegeta = Personaje("vegeta",99,99)
gogeta = goku + vegeta
print(gogeta)

#round es para redondear

