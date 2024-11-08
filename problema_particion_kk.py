
# Problema de partición con algoritmo Karmarkar-Karp

from bisect import insort
import time

def karmarkar_karp(conjunto):

    inicio = time.time()

    # Ordenar los números en orden ascendente
    conjunto.sort()
    
    while len(conjunto) > 1:
        num1 = conjunto.pop()
        num2 = conjunto.pop()
        diff = num1 - num2
        insort(conjunto, diff)
        

    fin = time.time()
    print(f'Diferencia mínima entre los subconjuntos: {conjunto[0]}')
    print(f'Tiempo de ejecución: {(fin-inicio): .10f}s')

    return conjunto[0]