class Estudiante:
    def __init__(self,Nombre,Edad,Grado):
     self.nombre = Nombre
     self.edad = Edad
     self.grado = Grado

    def estudiar(self):
     print(f'el estudiante {self.nombre} esta estudiando')





nom = input("ingrese el nombre: ")
eda = input("ingrese la edad: ")
grad = input("ingrese el grado: ")

estudiante1 = Estudiante(nom,eda,grad)

print(estudiante1.estudiar())