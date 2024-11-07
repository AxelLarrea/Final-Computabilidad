import json
from problema_particion_fb import fuerza_bruta
from problema_particion_g import greedy
from problema_particion_greedy_pd import greedy_pd

with open("data/datos1000.json", "r") as file:
    data = json.load(file)

if __name__ == '__main__':
    greedy_pd(data)