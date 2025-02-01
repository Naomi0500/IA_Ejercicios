def desglose_euros(cantidad):
    denominaciones = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    desglose = {}
    
    for billete_moneda in denominaciones:
        cantidad_billetes_monedas = cantidad // billete_moneda
        if cantidad_billetes_monedas > 0:
            desglose[billete_moneda] = cantidad_billetes_monedas
            cantidad %= billete_moneda
    
    return desglose

try:
    cantidad = int(input("Introduce una cantidad entera en euros: "))
    if cantidad <= 0:
        print("Por favor introduce un número mayor que cero.")
    else:
        desglose = desglose_euros(cantidad)
        
        print("Desglose en billetes y monedas:")
        for denominacion, cantidad in desglose.items():
            print(f"{denominacion}€: {cantidad}")
except ValueError:
    print("Por favor introduce un número entero válido.")
