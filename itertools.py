from itertools import accumulate, takewhile

# Generar lista con cuadrados y cubos
lista_numeros = [x**2 if x % 2 == 0 else x**3 for x in range(1, 101)]

# Calcular suma acumulativa usando itertools.accumulate
suma_acumulada = list(accumulate(lista_numeros))

# Filtrar los números cuya suma no exceda el límite de un millón
suma_valida = list(takewhile(lambda x: x < 1000000, suma_acumulada))

# Resultados finales
contador_numeros = len(suma_valida)
suma_final = suma_valida[-1] if suma_valida else 0

print(f"Se necesitan sumar {contador_numeros} números para acercarse a un millón sin pasarse.")
print(f"Suma acumulada: {suma_final}")
