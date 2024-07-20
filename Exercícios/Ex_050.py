"""
Desenvolva um programa que leia 6 números inteiros e mostre a soma daqueles que forem pares.

Se o valor digitado for ímpar, desconsidere-o
"""
print('')
print('\033[1;33m=-\033[m' * 20)
n2 = 0
for c in range(0, 6):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        n2 += n1
print(f'A soma dos números pares é: {n2}')
print('\033[1;33m=-\033[m' * 20)
print('')