def fibonacci(num):
    a,b = 0.1
    fibonacci_lista = [0]

    for i in range(num):
        if a+b > num: return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a,b = a,a+b
    return fibonacci_lista

resultado = fibonacci(20)
print(resultado)
        
        