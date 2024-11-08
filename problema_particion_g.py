
# Problema de partición con algoritmo Greedy

import time

def greedy(conjunto):
    
    subconjunto1 = []
    subconjunto2 = []
    suma1 = 0
    suma2 = 0
    
    inicio = time.time()
    
    conjunto.sort(reverse=True)
    
    
    # Asigna cada número al grupo con la suma más baja
    for number in conjunto:
        if suma1 <= suma2:
            subconjunto1.append(number)
            suma1 += number
        else:
            subconjunto2.append(number)
            suma2 += number
            
    fin = time.time()
    
    # print(f'Subconjunto A:{subconjunto1} - Subconjunto B:{subconjunto2}')
    print(f'Suma de cada subconjunto - Subconjunto A:{suma1} - Subconjunto B:{suma2}')
    print(f'Tiempo de ejecución: {(fin-inicio): .10f}s')

    return suma1-suma2