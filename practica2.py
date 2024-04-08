frase = input("decime  una frase: ")



palabras_separadas =  frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'dijiste {cantidad_de_palabras} palabras, y tardas {cantidad_de_palabras/2} separadas en decirlo')