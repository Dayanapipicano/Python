#METODOS ESPECIALES

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre = {self.nombre},edad = {self.edad})"

    def __add__(self,otro):
     nuevo_valor = self.edad + otro.edad
     return Persona(self.nombre + otro.nombre,nuevo_valor)
#sobre carga de operadores 
pedro = Persona("lucas",21)
daya = Persona("daya",18)

resultado = pedro + daya
print(resultado.nombre)