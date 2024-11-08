
# Algoritmo de Martello y Toth (1990) utilizando una combinación de 
# programación dinámica y el método greedy 

import time

def greedy_pd(conjunto):

    total = sum(conjunto)
    target = total // 2
    inicio = time.time()
        
    # Ordenar los pesos en orden descendente
    conjunto.sort(reverse=True)
    
    # Lista de sumas y sus subconjuntos correspondientes
    subset_sum = {0: []}
    
    for num in conjunto:

        new_subset = {}

        for s in list(subset_sum.keys()):
            new_num = s + num
            if new_num <= target and new_num not in subset_sum:
                # Guardar la nueva suma y el subconjunto que lleva a esta suma
                new_subset[new_num] = subset_sum[s] + [num]
        
        # Actualizar el diccionario de sumas con los nuevos subconjuntos
        subset_sum.update(new_subset)


    if target in subset_sum:

        subconjunto1 = subset_sum[target]
        subconjunto2 = conjunto.copy()
        
        for item in subconjunto1:
            subconjunto2.remove(item)

        fin = time.time()
        print('Existen dos subconjuntos que sumen lo mismo')
        # print(f'Solución - Subconjunto A:{subconjunto1} - Subconjunto B:{subconjunto2}')
        print(f'Suma de cada subconjunto - Subconjunto A:{sum(subconjunto1)} - Subconjunto B:{sum(subconjunto2)}')
        print(f'Tiempo de ejecución: {(fin-inicio): .10f}s')
    else:
        fin = time.time()
        print('No existen dos subconjuntos que sumen lo mismo')
        print(f'Tiempo de ejecución: {(fin-inicio): .10f}s')
