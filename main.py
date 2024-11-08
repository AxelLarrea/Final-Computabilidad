import json
from problema_particion_fb import fuerza_bruta
from problema_particion_g import greedy
from otros_algoritmos.problema_particion_greedy_pd import greedy_pd
from problema_particion_kk import karmarkar_karp
from porcentaje_error import porcentaje_error
from generar_datos import generateData

# generateData(500)

with open("data/datos10000.json", "r") as file:
    data = json.load(file)

total = sum(data)
# print(f'Total: {total}')

# if __name__ == '__main__':
#     # fuerza_bruta(data)
#     diferencia1 = greedy(data)
#     porcentaje_error(diferencia1, total)
#     print()
#     diferencia2 = karmarkar_karp(data)
#     porcentaje_error(diferencia2, total)
