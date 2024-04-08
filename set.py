conjunto = set(["dato1", "dato2"])

conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dalto"}

print(conjunto2)

conjunto3 = {1,2,5,7}
conjunto4 = {1,3,7}

resultado = conjunto3.issuperset(conjunto3)

print(resultado)