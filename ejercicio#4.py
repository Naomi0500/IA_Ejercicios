def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    secuencia = [0, 1]
    for i in range(2, n):
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

n = int(input("Introduce el número de términos de la sucesión de Fibonacci: "))
print(f"La sucesión de Fibonacci para n={n} es: {fibonacci(n)}")