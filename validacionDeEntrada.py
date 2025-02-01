def calcular_letra_dni(numero_dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    residuo = numero_dni % 23
    return letras[residuo]

while True:
    try:
        dni = int(input("Introduce tu número de DNI (sin letra): "))
        if dni < 0:
            print("El número de DNI no puede ser negativo. Inténtalo de nuevo.")
            continue
        letra = calcular_letra_dni(dni)
        print(f"La letra correspondiente a tu DNI es: {letra}")
        break
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")
