def generar_lista_cuadrados_cubos(rango):
    """Genera una lista de cuadrados y cubos según sea par o impar."""
    return [x**2 if x % 2 == 0 else x**3 for x in rango]

def calcular_suma(lista, limite):
    """Calcula cuántos números sumar para acercarse al límite sin pasarse."""
    suma_acumulada = 0
    contador_numeros = 0

    for numero in lista:
        if suma_acumulada + numero >= limite:
            break
        suma_acumulada += numero
        contador_numeros += 1

    return contador_numeros, suma_acumulada

# Parámetros
rango = range(1, 101)
limite = 1000000

# Ejecución
lista_numeros = generar_lista_cuadrados_cubos(rango)
contador_numeros, suma_acumulada = calcular_suma(lista_numeros, limite)

# Resultado
print(f"Se necesitan sumar {contador_numeros} números para acercarse a un millón sin pasarse.")
print(f"Suma acumulada: {suma_acumulada}")
