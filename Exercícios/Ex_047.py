"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo de 0 a 50.
"""
print('')
print('\033[1;33m-=\033[m' * 40)

for c in range(0, 50 + 2, 2):
    print(c, end = ' ')
print('Acabou')
print('\033[1;33m-=\033[m' * 40)
print('')