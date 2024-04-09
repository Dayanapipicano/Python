class Celular:
    
    #ESTO ES UN CONTRUCTOR DE LA CLASE 
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara


#ESTOS SON METODOS 

    def llamar(self):
     print(f'Estas haciendo un llamado {self.modelo}')

    def contar(self):
     print(f'Cortaste la llamada{self.modelo}')


#ESTE ES EL OBJETO
        
celular1 = Celular("samsung","s23", "48mp")
        

print(celular1.llamar())
