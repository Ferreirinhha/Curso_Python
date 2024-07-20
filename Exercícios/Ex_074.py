"""
Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor
e o mairo valor que estão na tupla.
"""
from random import randint

print('')
print('\033[1;33m=-\033m' * 30)

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10),randint(1,10))

print('Os elementos da tupla são: ', end="")
for i in numeros:
    print(i, end=" ")
print('')
print(f'Maior elemento da tupla: {max(numeros)}')
print(f'Maior elemento da tupla: {min(numeros)}')
print('\033[1;33m=-\033m' * 30)
print('')






