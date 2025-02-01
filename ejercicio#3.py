def calcular_pi(n):
    pi = sum([4 * ((-1) ** (k + 1)) / (2 * k - 1) for k in range(1, n + 1)])
    return pi

n = 200
valor_pi = calcular_pi(n)
print(f"El valor aproximado de π con n={n} es: {valor_pi:.10f}")