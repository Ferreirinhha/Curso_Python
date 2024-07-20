# Crie um programa que leia um número inteiro e diga se ele é ou não um número primo

print('')
print('\033[33m-=' * 12)
n1 = int(input('Digite um número: '))
cont = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print(f'\033[33m{c}\033[m', end = ' ')
        cont += 1
    else:
        print(f'\033[34m{c}\033[m', end = ' ')
if cont == 2:
    print(f' \nO número {n1} é primo.')
else:
    print(f' \nO número {n1} não é primo.')
print('\033[33m-=' * 12)
print('')
    