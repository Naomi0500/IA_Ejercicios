def calcular_letra_dni(numero_dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    residuo = numero_dni % 23
    return letras[residuo]

dni = int(input("Introduce tu número de DNI (sin letra): "))
letra = calcular_letra_dni(dni)
print(f"La letra correspondiente a tu DNI es: {letra}")