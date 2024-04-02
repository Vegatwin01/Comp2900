import unittest
import timeit

def max_lista(lista):
    return max(lista)

def max_iterativo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

# Definir una clase de pruebas para los enfoques
class TestMaximo(unittest.TestCase):

    # Prueba para el enfoque utilizando la función max()
    def test_max_lista(self):
        lista = [1, 2, 3, 4 ,5]
        tiempo_enfoque_1 = timeit.timeit(lambda: max_lista(lista), number=1000)
        print(f"Tiempo de ejecución para max_lista: {tiempo_enfoque_1} segundos")

    # Prueba para el enfoque iterativo
    def test_max_iterativo(self):
        lista = [1, 2, 3, 4, 5]
        tiempo_enfoque_2 = timeit.timeit(lambda: max_iterativo(lista), number=1000)
        print(f"Tiempo de ejecución para max_iterativo: {tiempo_enfoque_2} segundos")

if __name__ == '__main__':
    unittest.main()
