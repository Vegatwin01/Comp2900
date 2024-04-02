def suma_naturales(n):
    if n == 0:
        return 0
    else:
        return n + suma_naturales(n-1)

n1 = 20
resultado1 = suma_naturales(n1)
print(f"La suma de los primeros {n1} números naturales es: {resultado1}")  

n2 = 6
resultado2 = suma_naturales(n2)
print(f"La suma de los primeros {n2} números naturales es: {resultado2}")  
