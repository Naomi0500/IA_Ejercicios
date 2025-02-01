def calcular_pi(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("El valor de n debe ser un entero positivo.")
    pi = sum([4 * ((-1) ** (k + 1)) / (2 * k - 1) for k in range(1, n + 1)])
    return pi

try:
    n = 200
    valor_pi = calcular_pi(n)
    print(f"El valor aproximado de π con n={n} es: {valor_pi:.10f}")
except ValueError as e:
    print(e)
