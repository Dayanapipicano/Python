diccionario = {
    "nombre" : "lucas",
    "apellidos" : "dalto",
    "subs" : 10000
}

for datos in diccionario.items():

    key = datos[0]
    value = datos[1]

    print(f"la clave es: {key} y el valor es {value}")