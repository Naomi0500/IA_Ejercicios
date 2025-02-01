# Generar lista con cuadrados y cubos
lista_numeros = [x**2 if x % 2 == 0 else x**3 for x in range(1, 101)]

# Encontrar cuántos números sumar para acercarse a un millón sin pasarse
suma_acumulada = 0
contador_numeros = 0

for numero in lista_numeros:
    if suma_acumulada + numero >= 1000000:
        break
    suma_acumulada += numero
    contador_numeros += 1

print(f"Se necesitan sumar {contador_numeros} números para acercarse a un millón sin pasarse.")
print(f"Suma acumulada: {suma_acumulada}")
