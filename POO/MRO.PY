class a:
    def hablar(self):
        print("hola desde A")

class b(a):
    
    def hablar(self):
     print("hola desde B")
     
class c(a):
    def hablar(self):
        print("hola desde c")
        
class D(b,c):
    def hablar(self):
        print('hola desde D')


de = D()

de.hablar()