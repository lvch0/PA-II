entrada = int(input("Ingrese un número entero del 0 al 255:"))

if (entrada > 0 and entrada < 255):
    binario = bin(entrada)
    print(binario)
else:
    print("El valor ingresado está fuera de rango")