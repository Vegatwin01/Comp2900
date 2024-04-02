def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)

base1 = 2
exponente1 = 5
resultado1 = potencia(base1, exponente1)
print(f"{base1} elevado a la {exponente1} es igual a: {resultado1}")  

base2 = 3
exponente2 = 4
resultado2 = potencia(base2, exponente2)
print(f"{base2} elevado a la {exponente2} es igual a: {resultado2}")  