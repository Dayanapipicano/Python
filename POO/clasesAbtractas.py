from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} mi edad es {self.edad}")


class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        print(f"estoy estudiando: {self.actividad}")
        
        
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        print(f"estoy trabajando: {self.actividad}")
    
dalto = Estudiante("lucas",21,"masculino","programador")
pedro = Trabajador("pepe",21,"masculino","programador")

dalto.hacer_actividad()
dalto.presentarse()
pedro.presentarse()
pedro.hacer_actividad()       
        
        
