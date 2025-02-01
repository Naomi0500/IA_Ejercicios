def fibonacci_recursivo(n):
    """
    Calcula el término n-ésimo de la sucesión de Fibonacci usando recursividad.
    :param n: Número entero positivo.
    :return: Término n-ésimo de Fibonacci.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Llamadas recursivas para construir la lista completa
    secuencia = fibonacci_recursivo(n - 1)
    secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

# Solicitar al usuario el número de términos
n = int(input("Introduce el número de términos de la sucesión de Fibonacci (recursiva): "))
print(f"La sucesión de Fibonacci para n={n} es: {fibonacci_recursivo(n)}")
