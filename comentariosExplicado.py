def fibonacci(n):
    """
    Genera la sucesión de Fibonacci hasta el n-ésimo término.
    :param n: Número de términos de la sucesión.
    :return: Lista con los términos de la sucesión de Fibonacci.
    """
    if n <= 0:
        return []  # Caso base: si n es menor o igual a 0, devuelve una lista vacía.
    elif n == 1:
        return [0]  # Caso base: si n es 1, devuelve [0].
    elif n == 2:
        return [0, 1]  # Caso base: si n es 2, devuelve [0, 1].
    
    # Construcción de la secuencia para n > 2
    secuencia = [0, 1]
    for i in range(2, n):
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

# Solicitar al usuario el número de términos
n = int(input("Introduce el número de términos de la sucesión de Fibonacci: "))
print(f"La sucesión de Fibonacci para n={n} es: {fibonacci(n)}")
