
animales = ["perro","loro","gato"]

for animal in animales:
    print(f"animal es igual a{animal}")

numeros = [52,16,14,72]
for numero,animal in zip(numeros,animales):
    print(f"recorriemdo lista 1: {numero}")
    print(f"recorriemdo lista 2: {animal}")


""" for num in range(5,10):
    print(num) """


for num in enumerate(numeros):
    print(num)

for numero in numeros:
    print(f"ultimo bucle: {numero}")
else:
    print("el bucle termino")