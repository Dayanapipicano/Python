""" def obtenercompañeros(cantidad_de_compañeros):
    compañeros = []

    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero")
        edad = int(input("ingrese la edad del compañero"))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente,profesor = obtenercompañeros(5)

print(f"el profesor{profesor} y asistente es {asistente}")
 """

""" def es_primo(num):
    for i in range(2,num-1):
        if num%i==0 : return False
    return True """

"""   esta es una manera de ir 
    agregando los resultados a un lista cuando 
    los corremos por bucle for """
""" def primos_hasta(num):
  
    primos = []
    for i in range(3,num+1):
        resultado = es_primo(i)

    #y asi es como debe de ser

        if resultado == True: primos.append(i)
    return primos
resultado = primos_hasta(99)
print(resultado) """
    

""" def mult(num):
  
    for i in range(1,11):
        res = num * i
        i = i + 1
        print(f"{num} x {i}={res}")
    
    

mult(5)
 """



