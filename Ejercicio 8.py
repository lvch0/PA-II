import random

num = random.randint(1, 100)
entrada = int(input("Ingrese un valor que se encuentre entre 1 y 100:"))
intentos = 10

while(intentos != 0):
    if(entrada == num):
        print("¡¡¡Felicitaciones, haz acertado!!!")
        break
    elif(entrada < num):
        print("Nuestro valor ingresado es menor que el número generado al azar.")
    elif(entrada > num):
        print("Nuestro valor ingresado es mayor que el número generado al azar ")
    else:
        print("Por favor ingrese un valor del 1 al 100")
        break
    
    intentos -= intentos
    print(f"Le quedan {intentos} intentos.")
    
    
    
