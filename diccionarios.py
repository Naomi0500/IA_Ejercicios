def calcular_letra_dni(numero_dni):
    letras = {
        0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y",
        7: "F", 8: "P", 9: "D", 10: "X", 11: "B", 12: "N",
        13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H",
        19: "L", 20: "C", 21: "K", 22: "E"
    }
    residuo = numero_dni % 23
    return letras[residuo]

def main():
    try:
        dni = int(input("Introduce tu número de DNI (sin letra): "))
        if dni < 0:
            print("El número de DNI no puede ser negativo.")
            return
        letra = calcular_letra_dni(dni)
        print(f"La letra correspondiente a tu DNI es: {letra}")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")

if __name__ == "__main__":
    main()
