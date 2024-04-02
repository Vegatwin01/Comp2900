def coeficiente_binomial(n, k):
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    return coeficiente_binomial(n-1, k-1) + coeficiente_binomial(n-1, k)

n1 = 5
k1 = 2
resultado1 = coeficiente_binomial(n1, k1)
print(f"El coeficiente binomial de {n1} tomados de {k1} en {k1} es: {resultado1}") 
