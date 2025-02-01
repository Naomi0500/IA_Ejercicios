import math
import unittest

def calcular_temperatura(Ts, T0, k, t):
    return Ts + (T0 - Ts) * math.exp(-k * t)

def tiempo_para_temperatura_optimizado(Ts, T0, k, T_deseada):
    if T_deseada >= Ts:
        return 0
    return -math.log((T_deseada - Ts) / (T0 - Ts)) / k

# Pruebas unitarias
class TestCalculos(unittest.TestCase):
    
    def test_calcular_temperatura(self):
        self.assertAlmostEqual(calcular_temperatura(40, 5, 0.45, 1), 17.24, places=2)
        self.assertAlmostEqual(calcular_temperatura(40, 5, 0.45, 5), 36.15, places=2)
    
    def test_tiempo_para_temperatura(self):
        self.assertAlmostEqual(tiempo_para_temperatura_optimizado(40, 5, 0.45, 39.5), 7.69, places=2)
        self.assertEqual(tiempo_para_temperatura_optimizado(40, 5, 0.45, 40), 0)

if __name__ == "__main__":
    # Ejecutar pruebas unitarias
    unittest.main()
