
# Problema de partición con Fuerza Bruta 

import time
from itertools import combinations


def fuerza_bruta(conjunto):

	total = sum(conjunto)
	mitad = total//2
	subconjuntos = []
	
	inicio = time.time()

	if (total % 2 == 0):
		for i in range(0, len(conjunto)+1):
 
			for subconjunto in combinations(conjunto, i):
				if (sum(subconjunto)==mitad):
					subconjunto2 = conjunto.copy()
					for num in subconjunto:
						# Cada número del subconjunto de las combinaciones es eliminado en el subconjunto2
						# el cual tiene una copia del conjunto original
						subconjunto2.remove(num)
					subconjuntos.append([list(subconjunto), subconjunto2])
		fin = time.time()

		if len(subconjuntos)>0:
			print('Existen dos subconjuntos que sumen lo mismo')
			# for i in range(0, len(subconjuntos)//2):
			# 	print(f'Solución {i+1} - Subconjunto A:{subconjuntos[i][0]} - Subconjunto B:{subconjuntos[i][1]}')
			print(f'Cantidad de elementos en el conjunto: {len(conjunto)}')
			print(f'Suma de cada subconjunto - Subconjunto A:{sum(subconjuntos[0][0])} - Subconjunto B:{sum(subconjuntos[0][1])}')
			print(f'Tiempo de ejecución: {(fin-inicio): .10f}s')
		else:
			print('No existen dos subconjuntos que sumen lo mismo')
			print(f'Tiempo de ejecución: {(fin-inicio):.10f}s')
	else:
		fin = time.time()
		print('La suma del conjunto no se puede dividir a la mitad')
		print(f'Tiempo de ejecución: {(fin-inicio):.10f}s')