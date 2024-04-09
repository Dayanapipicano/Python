class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
        
    #no se plvide del self en el metodo
    def hablar(self):
     print("hola estoy hablando")
        
        
""" class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo, salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
 """

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
    #POR DIOS EL SELF EN EL METODO NO PUEDE FALTAR EHHHHHH  
    def mostrar_habilidad(self):
        print(f"mi habilidad es: {self.habilidad}")
    
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
       Persona.__init__(self,nombre,edad,nacionalidad)
       Artista.__init__(self,habilidad)
       self.salario = salario
       self.empresa = empresa
    
    def presentarse(self):
        print(f'{super().mostrar_habilidad()}')

roberto = EmpleadoArtista("roberto",43,"argentino","programador","100000","google")
 
herencia = issubclass(EmpleadoArtista,Artista)
print(herencia)

instancia = isinstance(roberto,EmpleadoArtista)
print(instancia)


print(roberto.presentarse())