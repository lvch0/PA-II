from re import I
import numpy as np
array = np.array([])
i = 0

while (i < 10):
    entrada = int(input("Ingrese 10 valores enteros: "))
    array[i] = entrada
    i += 1

for n in array:
    if (n % 2 == 0):
        print(entrada + " ", end="")
    


