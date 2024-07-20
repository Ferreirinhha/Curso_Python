"""
Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:

O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais
"""
print('')
print('\033[1;33m-=\033[m' * 25)
n1 = int(input('\033[1;33mDigite o primeiro número:\033[1;35m '))
n2 = int(input('\033[1;33mDigite o segundo número:\033[1;35m '))

if n1 > n2:
    print('')
    print(f'\033[1;33mO número \033[1;4;35m{n1}\033[m \033[1;33mé maior que \033[1;4;35m{n2}\033[m')
    print('')
elif n2 > n1:
    print('')
    print(f'\033[1;33mO número \033[1;4;35m{n2}\033[m \033[1;33mé maior que \033[1;4;35m{n1}\033[m')
    print('')
else:
    print('')
    print(f'\033[1;33mO número \033[1;4;35m{n1}\033[m \033[1;33mé igual a \033[1;4;35m{n2}\033[m')
print('\033[1;33m-=\033[m' * 25)
print('')
