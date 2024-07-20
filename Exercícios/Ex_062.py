"""
Melhore o desafio 61, perguntando para o usuárop se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.

Desafio 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão.
"""
print('')
print('\033[1;33m-=\033[m' * 30)

n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
continuar = ''
termo = 0

while cont <= 10 + termo or continuar == 'SIM':
    print(n1, end=" → ")
    n1 += razao
    cont += 1
    if cont > 10 + termo:
        continuar = str(input('\n Quer continuar: ')).upper().strip()
        if continuar == 'SIM':
            termo = int(input('Quantos termos: '))
print(f'Termos impreços: {cont - 1}')
print('Fim.')
print('\033[1;33m-=\033[m' * 30)
print('')
