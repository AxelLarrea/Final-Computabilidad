import matplotlib.pyplot as plt


# Punto 4 
# Gráfico del tiempo de ejecución con respecto a la cantidad de elementos

# cantidad = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
#         21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

# segundos = [0.0001, 0.0002, 0.0005, 0.0021, 0.0023, 0.0046, 0.0091, 0.0185,
#        0.0388, 0.0771, 0.1644, 0.3264, 0.7482, 1.4250, 2.9352, 6.3692,
#        12.4722, 25.7482, 52.9839, 109.5469, 375.4385, 1015.3084]


# plt.figure(figsize=(8,5))
# plt.plot(cantidad, segundos)
# plt.xlabel('Cantidad de elementos')
# plt.ylabel('Tiempo de ejecución (segundos)')
# plt.title('Método Fuerza Bruta')
# plt.show()


# Punto 5
# Greedy

# cantidad = [1000, 2000, 3000, 4000, 5000, 7500, 10000]

# segundos = [0.0001, 0.0002, 0.0003, 0.0004, 0.0005, 0.0007, 0.0010]


# Algoritmo de Karmarkar-Karp

cantidad = [1000, 2000, 3000, 4000, 5000, 7500, 10000]

segundos = [0.0002, 0.0005, 0.0010, 0.0017, 0.0025, 0.0050, 0.0087]


plt.figure(figsize=(8,5))
plt.plot(cantidad, segundos)
plt.xlabel('Cantidad de elementos')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Algoritmo de Karmarkar-Karp')
plt.show()