cadena1 = input("Ingrese una cadena:")
cadena2 = input("Ingrese una subcadena de la cadena anteriormente ingresada:")

subcadena = cadena1.find(cadena2)

if(subcadena >= 0):
    print("La subcadena se encuentra a partir de la posición ", subcadena)
else:
    print("La subcadena no se encuentra dentro de la cadena")


