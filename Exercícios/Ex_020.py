"""
O mesmo professor quer sortear a ordem de apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatroa lunos e mostre a orfem sorteada
"""

import random

g1 = input('Grupo 1: ')
g2 = input('Grupo 2: ')
g3 = input('Grupo 3: ')
g4 = input('Grupo 4: ')

deck = [g1,g2,g3,g4]

a= random.shuffle(deck)                    
print(f'A ordem dos grupos ficara com: {deck}')