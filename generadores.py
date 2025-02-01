def fibonacci_generador(n):
    """
    Generador que produce los términos de la sucesión de Fibonacci.
    :param n: Número entero positivo.
    :yield: Términos consecutivos de la sucesión.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Solicitar al usuario el número de términos y mostrar los resultados
n = int(input("Introduce el número de términos de la sucesión de Fibonacci (generador): "))
print(f"La sucesión de Fibonacci para n={n} es: {list(fibonacci_generador(n))}")
