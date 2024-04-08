numeros = {
    "uno" : "one",
    "dos" : "two",
    "tres" : "there",
    "cuatro" : "four",
    "cinco" : "five"
}

for num in numeros:
    print(num)


nums = numeros["tres"]

print(f" el valor es: {nums}")

num1 = numeros["cinco"] = 5

print(f" el valor editado es: {num1}")

numeros["seis"] = "six"

print(numeros)



numeros.pop("uno")
print(numeros)