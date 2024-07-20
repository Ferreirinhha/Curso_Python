"""
Crie um programa onde 4 jogadores jogue um dado e tenham resultados aleatório. No final coloque esses
resultados em um dicionário. No final coloque esse dincionário em ordem, sabendo que o vencedor tirou o
maior número no dado.
"""

import random
import operator

podium = dict()

for i in range(1, 5):
    n = random.randint(1, 6)
    if i > 0:
        podium[f'Player {i}'] = n

ranking = list()
ranking = sorted(podium.items(), key=operator.itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'O {i + 1}° lugar: {v[0]} com {v[1]} pontos.')

print(ranking)
