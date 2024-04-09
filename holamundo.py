
#kw arbs permite un numero de argumentos variables con clave 
#argumentos posicionales. y los otros solo tinen un nombre y un valor diccionario, estructura de clave valor

""" 
def claves(**kwargs):
    numero = 0
    for clave in kwargs.values():
        numero +=1
        print(f"clave {numero}: {clave}")
        
claves(nombre="javier", apellidos="gomez", edad="32")
 """

#posicionales y otro de clave 

#para la clave es keys
#para el vzlor es "¿values"
#y para ambos es items 

def sumar(*args):
    
    
   
    print(args[0] + args[1] + args[2]) 
    
valor = [10,7,4]
sumar(1,2,3)


def res(**kwargs):
    
    
    
   clave = tuple(kwargs.keys())
    
   print(f"el {clave[0]} es:{kwargs["nombre"]}, sus apellidos son: {kwargs["apellidos"]}, y tiene {kwargs["edad"]} años")


li = {"nombre":"javier","apellidos":"gomez","edad":"27"}
res(**li)