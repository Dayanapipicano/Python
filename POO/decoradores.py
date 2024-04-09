def decorador(funcion):
    def funcion_modificada():
        print("antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada 

# def saludo():
#  print("hola dalto como antes")

# saludo_mod = decorador(saludo)
# saludo_mod()

@decorador
def saludo():
    print("hola dalto como antes")
    
saludo()