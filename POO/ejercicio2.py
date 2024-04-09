class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def nombre_edad(self):
        print(f"el nombre es: {self.nombre} y la edad es: {self.edad}")
        
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre,edad)
        self.grado = grado
        
    def grados(self):
        print(f"el grado es: {self.grado}")
       
    
estudiante1 = Estudiante("daya","12","11")

print(estudiante1.nombre_edad())