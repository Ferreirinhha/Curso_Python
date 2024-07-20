"""
Faça um programa que mostre a soma de todos os números impáres que são multiplos de 3 e que se encontram no
intervalo de 1 a 500.
"""
print('')
print('\033[1;33m-=\033[m' * 40)

soma = 0

for c in range(0, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            print(c, end = ' ')
            soma += c
print(f'\n A soma de todos os numeros da {soma}')
print('\033[1;33m-=\033[m' * 40)
print('')           

    