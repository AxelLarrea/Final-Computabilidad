import json
import random

def generateData(n):
    data = [ random.randint(1, 10) for _ in range(n) ]
    
    with open("datos.json", "w") as file:
        json.dump(data, file, indent=4)


# n = 7500
# generateData(n)