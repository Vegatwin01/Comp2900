import unittest
import time

def suma_for(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

def suma_formula(n):
    return (n * (n+1)) // 2

class TestSuma(unittest.TestCase):
    def test_suma_for(self):
        self.assertEqual(suma_for(5), 15)  # Prueba básica
        self.assertEqual(suma_for(10), 55)  # Otra prueba

    def test_suma_formula(self):
        self.assertEqual(suma_formula(5), 15)  # Prueba básica
        self.assertEqual(suma_formula(10), 55)  # Otra prueba

def medir_tiempo_suma(func, n):
    inicio = time.time()
    resultado = func(n)
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return resultado, tiempo_ejecucion

if __name__ == '__main__':
    n = 1000000  # Número para el cual realizar la suma
    resultado_for, tiempo_for = medir_tiempo_suma(suma_for, n)
    resultado_formula, tiempo_formula = medir_tiempo_suma(suma_formula, n)

    print(f"Resultado usando ciclo for: {resultado_for}, Tiempo: {tiempo_for} segundos")
    print(f"Resultado usando fórmula matemática: {resultado_formula}, Tiempo: {tiempo_formula} segundos")

    unittest.main()

