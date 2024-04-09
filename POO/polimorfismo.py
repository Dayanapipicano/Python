class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"
    
    

def hacer_sonido(animal):
    print(f"desde hacer sonido {animal.sonido()}")


gato = Gato()
perro = Perro()

hacer_sonido(perro)

print(perro.sonido())
print(gato.sonido())