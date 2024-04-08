from abc import ABC, abstractmethod

class Animales(ABC):
    @abstractmethod

    
    def ir(self):
        pass


class leon(Animales):
    def ir(self):
        print('animal salvaje')

class perro(Animales):
    def ir(self):
        print('animal domestico')


leon = leon()
perro = perro()


leon.ir()
perro.ir()

