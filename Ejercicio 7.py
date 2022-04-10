binario = input("Ingrese una cifra binaria: ")
longitud = len(binario) - 1
calculo = 0
entero = 0

for num in binario:
    if(num == "1"):
        calculo = (int(num) * 2) ** longitud
        entero += calculo
    elif(num == "0"):
        calculo = 0
    else:
        print("Recuerde que la cifra debe ser binaria.")
        break      
    longitud -= 1
    
print(f'Binario: {binario}\nEntero: {entero}')
        