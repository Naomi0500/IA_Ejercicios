def calcular_pi_recursivo(k, n, acumulado=0):
    if k > n:
        return acumulado
    termino = 4 * ((-1) ** (k + 1)) / (2 * k - 1)
    return calcular_pi_recursivo(k + 1, n, acumulado + termino)

def calcular_pi(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("El valor de n debe ser un entero positivo.")
    return calcular_pi_recursivo(1, n)

try:
    n = 200
    valor_pi = calcular_pi(n)
    print(f"El valor aproximado de π con n={n} es: {valor_pi:.10f}")
except ValueError as e:
    print(e)
