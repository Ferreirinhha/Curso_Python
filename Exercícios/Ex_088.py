"""
Faça um programa que ajude um jogador da megasena e faça palpites. O jogador irá
dizer quantos jogos serão sorteados e vai sortear 6 numeros de 0 a 60, para cada
jogo e cadastrando tudo em uma lista
"""

from random import randint
from time import sleep

mega = list()
jogos = list()

num_sorteios = int(input('Quantos jogos vai fazer: '))

for sorteio in range(1, num_sorteios + 1):
    cont = 0
    print('=' * 30)
    print(f'Jogo \033[1;4;{30 + sorteio}m{sorteio}\033[m: ', end=" ")
    print('[', end=' ')
    while True:
        palpites = randint(0, 60)
        if palpites not in jogos: 
            jogos.append(palpites)
            cont += 1
        print(palpites, end=" ")
        if cont == 6:
            break
    print(']', end=' ')
    mega.append(jogos[:])
    jogos.clear()
    print()
print()
print(f'Todos os jogos: {mega}') 