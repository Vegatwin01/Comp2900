# Enfoque 1: Usando un ciclo for
def search_for(number, numbers):
    for i in range(len(numbers)):
        if numbers[i] == number:
            return i
    return -1

# Enfoque 2: Usando la función index()
def search_index(number, numbers):
    try:
        return numbers.index(number)
    except ValueError:
        return -1

import timeit

numeros = list(range(10000))

numero_buscado = 9999

# Prueba de tiempo para el Enfoque 1
tiempo_enfoque_1 = timeit.timeit(lambda: search_for(numero_buscado, numeros), number=1000)

# Prueba de tiempo para el Enfoque 2
tiempo_enfoque_2 = timeit.timeit(lambda: search_index(numero_buscado, numeros), number=1000)

print(f"Tiempo de ejecución Enfoque 1: {tiempo_enfoque_1} segundos.")
print(f"Tiempo de ejecución Enfoque 2: {tiempo_enfoque_2} segundos.")

if tiempo_enfoque_1 < tiempo_enfoque_2:
    print("El Enfoque 1 (usando un ciclo for) es más eficiente en tiempo.")
else:
    print("El Enfoque 2 (usando la función index()) es más eficiente en tiempo.")

