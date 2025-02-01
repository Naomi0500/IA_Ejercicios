import math

def calcular_temperatura(Ts, T0, k, t):
    return Ts + (T0 - Ts) * math.exp(-k * t)

def tiempo_para_temperatura_optimizado(Ts, T0, k, T_deseada):
    # Resolviendo la ecuación para t: T_deseada = Ts + (T0 - Ts) * exp(-k * t)
    if T_deseada >= Ts:
        return 0  # Si la temperatura deseada es mayor o igual a la ambiente
    return -math.log((T_deseada - Ts) / (T0 - Ts)) / k

# Parámetros
Ts = 40  # Temperatura ambiente
T0 = 5   # Temperatura inicial
k = 0.45

# Calcular temperaturas para 1, 5, 12 y 14 horas
horas = [1, 5, 12, 14]
for h in horas:
    print(f"Temperatura a las {h} horas: {calcular_temperatura(Ts, T0, k, h):.2f} ºC")

# Calcular tiempo para que la temperatura esté a 0.5ºC menos que la temperatura ambiente
T_deseada = Ts - 0.5
tiempo = tiempo_para_temperatura_optimizado(Ts, T0, k, T_deseada)
print(f"Tiempo necesario para alcanzar {T_deseada} ºC: {tiempo:.2f} horas")
