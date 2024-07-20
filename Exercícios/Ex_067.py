"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para
cafa valor digitado pelo usuário. O programa será interrompido quando o número
solicitado for negativo.
"""
print('')
print('\033[1;33m-=\033[m' * 30)

cont = 0

while True:
    if cont == 0:
        n1 = int(input('Qual tabuada gostaria de ver ( Para sair, digite [-1] ): '))

    while cont < 10 and n1 >= 0:
        cont += 1
        print(f'{n1} * {cont} = {n1 * cont}')

    cont = 0
    print('')

    if n1 < 0:
        break
print('Fim.')
print('\033[1;33m-=\033[m' * 30)
print('')
