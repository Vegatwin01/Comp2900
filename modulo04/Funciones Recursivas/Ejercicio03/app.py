def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

num1 = 24
num2 = 20
resultado1 = mcd(num1, num2)
print(f"El máximo común divisor de {num1} y {num2} es: {resultado1}")  
