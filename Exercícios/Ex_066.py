"""
Crie um programa que leia vários números inteiros no teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final mostre
quantos números foram digitados e qual foi a soma entre eles. (desconsiderando o flag)
"""
cont = 0
soma = 0
print('')
print('\033[1;33m-=\033[m' * 30)
while True:
    n1 = int(input('Digite um número: '))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print(f'{cont} números foram digitados e a soma total é {soma}')
print('Fim.')
print('\033[1;33m-=\033[m' * 30)
print('')