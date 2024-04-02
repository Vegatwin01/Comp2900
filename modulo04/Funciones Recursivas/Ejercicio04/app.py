def invertir_cadena(cadena):
    if len (cadena) == 0:
        return ""
    else:
        return cadena [-1] + invertir_cadena(cadena[:-1])
    
cadena01 = "Hello World!"
resultado01 = invertir_cadena (cadena01)
print (f"El inverso de '{cadena01}' es {resultado01}")

cadena02 = "Bryan Vega" 
resultado02 = invertir_cadena (cadena02)
print (f"El inverso de '{cadena02}' es {resultado02}")