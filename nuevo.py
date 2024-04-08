""" def notas(nota1): #parametro
    if nota1 == 50:
        print("aprobado")
    elif nota1 == 40:
        print("satisfactorio")
    elif nota1 == 30:
        print("regular")
    elif nota1 == 10:
        print("reprobado")

    
    
notas(50) #argumentos
 """
""" def puntuacion(clase):
    return sum(clase) / len(clase)
   
clase = [10,20,30]
res = puntuacion(clase)
print(res)
 """
#se puede pasar como parametro una lista cuando son muchos valores
#la funcion sum() me suma todo


""" def multi(numero):
    for f in range(1,11):
        mult = numero * f
        print(f"numero: {numero} x {f} = {mult}")


multi(5)
 """
""" 
def cambio(numero):
    for i in range(numero):
       res = numero * i 
    return res

lu = cambio(4)

print(lu) """

""" 
def muetra(num):
    res = sum(num) / len(num)
    return res

lu = muetra([5,6,7])
print(lu)
 """

""" anchura = int(input("anchura:"))
altura = int(input("altura:"))
for i in range(altura):
    for j in range(anchura):
        print("*", end="")
    print() """

""" def calculo(num):
    print(min(num))

calculo([1,6,33])

def redondear(): 

 """
""" numero = round(12.8383,3)

print(numero)
 """

""" 
numero = all([])

print(numero)

numero = bool("f")

print(numero) """




def saludar():
    print("hola")

saludar()


def calculo(num):
    lista = "adcdfghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num - 3
    c3 = num - 5
    contraseña = f"{lista[c1]}{lista[c2]}{lista[c3]}{num*2}"
    print(contraseña)


   
calculo(98)
      
""" 
def suma(a,b):
    return a + b

suma(1,5)

 """

 #parametro args , tiene que ir adelante de args para quefuncones 
def suma(nombre, *numeros):
    return f"{nombre} la suma de los numeros es {sum(numeros)}"

resultado = suma("daya",1,3,4,5)
print(resultado)


nombre = lambda x : x*2


print(nombre(5))




numeros = [1,2,3,4,5,6,7,8,9]

""" def par(num):
   if(num%2==0):
    return True """



numeros_pare =filter(lambda numero:numero%2 == 0, numeros)
print(list( numeros_pare))





















