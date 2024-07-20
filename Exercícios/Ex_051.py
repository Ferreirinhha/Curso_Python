"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão.
"""
print('')
print('\033[33m-=\033[m' * 30)
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
r2 = 0

n_esimo_termo = p1 + (10 - 1) * razao #Formula do enesimo numero

for c in range(p1, n_esimo_termo + razao, razao):
    print(c, end = ' \u2192 ')
print('')
print('Acabou')
print('\033[33m-=\033[m' * 30)
print('')