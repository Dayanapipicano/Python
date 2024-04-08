numeros = (1,2,3,4,5,6,7,8,9,10)

for num in numeros:
    print(num)


print(f"el numero es: {numeros[4]}")

numeros = list(numeros)

numeros.append(12)

res = tuple(numeros)

print(res)

nuevo =("hola",)

print(nuevo)

frutas = set(["pera","mango","piña","banano"])

print(frutas)

frutas.remove("pera")
print(frutas)



