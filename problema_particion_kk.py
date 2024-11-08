from bisect import insort
import time

def karmarkar_karp(numbers):

    inicio = time.time()

    # Ordenar los números en orden ascendente
    numbers.sort()
    print(numbers)
    while len(numbers) > 1:
        num1 = numbers.pop()
        num2 = numbers.pop()
        diff = num1 - num2
        insort(numbers, diff)

    fin = time.time()
    print(f'Diferencia mínima entre los subconjuntos: {numbers}')
    print(f'Tiempo de ejecución: {fin-inicio}s')