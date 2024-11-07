
# Problema de partición con algoritmo Greedy

import time


def greedy(conjunto):
    
    group1 = []
    group2 = []
    suma1 = 0
    suma2 = 0
    
    inicio = time.time()
    
    conjunto.sort(reverse=True)
    
    # Asigna cada número al grupo con la suma más baja
    for number in conjunto:
        if suma1 <= suma2:
            group1.append(number)
            suma1 += number
        else:
            group2.append(number)
            suma2 += number
    fin = time.time()
    
    if (abs(sum(group1) - sum(group2)) == 0):
        print('Existen dos subconjuntos que sumen lo mismo')
        print(f'Suma de cada subconjunto - Subconjunto A:{suma1} - Subconjunto B:{suma2}')
        # print(f'Solución - Subconjunto A:{group1} - Subconjunto B:{group2}')
        print(f'Tiempo de ejecución: {(fin-inicio): .10f}s')
    else:
        print('No existen dos subconjuntos que sumen lo mismo')
        print(f'Tiempo de ejecución: {(fin-inicio): .10f}s')