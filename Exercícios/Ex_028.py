"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar adivinhar.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

import random
import time

n1 = random.randint(0, 5)

print('\033[1;33m-=-\033[m' * 20)
print('\033[1;35mPensei num número de 0 a 5...\033[m')
print('\033[1;33m-=-\033[m' * 20)

n2 = int(input('\033[1;40mTente advinhar no número que pensei: '))
print('PROCESSANDO...')
time.sleep(2)

if n1 == n2:
    print('\033[1;32mMeus parabéns, como adivinhou?')
else:
    print('\033[1;31mPutz, não foi desta vez, tente denovo.')