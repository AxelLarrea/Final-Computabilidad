
#Problema de partición con Algoritmo Genético

import random, time


def fitness(partition):
    """ Función para calcular la aptitud del cromosoma """

    # Calcula la diferencia entre las sumas de dos grupos
    group1_sum = sum(partition[0])
    group2_sum = sum(partition[1])
    return abs(group1_sum - group2_sum)

def crear_individuo(elements):
    """ Función para crear un cromosoma aleatoriamente """

    # Crea un cromosoma asignando de manera aleatoria los elementos del array a cada subconjunto
    individual = [[], []]
    for element in elements:
        individual[random.randint(0, 1)].append(element)
    return individual

def crossover(parent1, parent2):
    """ Función para combinar dos cromosomas, es decir, los subconjuntos de cada cromosoma """

    # Por ejemplo, si crossover_point es 3 y tenemos 10 elementos en cada subconjunto sc1, sc2 a combinar
    # entonces tendríamos desde el índice 0 hasta 3 de sc1, con los elementos desde el índice
    # 3 hasta el final de sc2, con esto se generaría un nuevo cromosoma (dos subconjuntos nuevos). 
    # Luego de esto se hace el caso contrario para generar el segundo cromosoma, cambiando de lugar los subconjuntos, quedaría por tanto
    # desde el índice 0 hasta 3 de sc2 y desde el índice 3 hasta el final de sc1. 

    # Combina dos cromosomas para crear descendientes
    crossover_point = random.randint(0, len(parent1[0]) - 1)
    child1 = [parent1[0][:crossover_point] + parent2[0][crossover_point:], 
               parent1[1][:crossover_point] + parent2[1][crossover_point:]]
    
    child2 = [parent2[0][:crossover_point] + parent1[0][crossover_point:], 
               parent2[1][:crossover_point] + parent1[1][crossover_point:]]
    
    return child1, child2

def mutar_individuo(individual):
    """ Función para mutar un individuo aleatoriamente """

    # Mutación aleatoria de un individuo, remueve un elemento de un subconjunto y se lo asigna al otro subconjunto

    if random.random() < 0.1:  # Probabilidad de mutación
        group = random.randint(0, 1)
        if individual[group]:
            number = random.choice(individual[group])
            individual[group].remove(number)
            individual[1 - group].append(number)


def algoritmo_genetico(numbers, population_size=1000, generations=1000):

    # Inicializa la población con cromosomas aleatorios
    population = [crear_individuo(numbers) for _ in range(population_size)]
    
    for generation in range(generations):
        population.sort(key=fitness)  # Ordenar por fitness (menor diferencia)
        next_generation = population[:population_size // 10]  # Selección de los mejores
        
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(next_generation[:20], 2)  # Selección aleatoria de padres entre los 20 mejores de la población
            children = crossover(parent1, parent2)
            next_generation.extend(children) # Se agrega el nuevo cromosoma resultante del crossover a la siguiente generación
        
        for individual in next_generation:
            mutar_individuo(individual)
        
        population = next_generation
    
    best_solution = min(population, key=fitness)
    return best_solution

# Ejemplo de uso
numbers = [3, 3, 4, 2, 2, 1, 5, 7, 7, 10, 32]
inicio = time.time()
solution = algoritmo_genetico(numbers)
fin = time.time()
print("Mejor partición encontrada:", solution)
print("Diferencia entre grupos:", fitness(solution))
print("Tiempo de ejecución: ", fin-inicio, "seg")