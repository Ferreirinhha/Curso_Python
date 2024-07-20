"""
Refaça o desafio 51 lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.
"""
print('')
print('\033[1;33m-=\033[m' * 30)
n1 = int(input('Primeiro termo: '))
razao = int(input('Qual razão: '))
cont = 1

while cont <= 10:
    print(n1, end=" → ")
    n1 += razao
    cont += 1
print('\033[1;33m-=\033[m' * 30)
print('')