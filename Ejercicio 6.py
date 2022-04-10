entero = int(input("Ingrese un valor entero de 0 a 255:"))
binario = ""

if(entero > 0 and entero < 255):
    while(entero -1 != 0):
        if(entero % 2 == 0):
            binario += "0"
            entero /= 2
        else:
            binario += "1"
            entero = int(entero / 2)
    binario += "1"
    binario = binario[::-1]
    print(binario)
    
    