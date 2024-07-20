"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio,
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa 
vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print('')
print('\033[1;33m-=\033[m' * 30)

n1 = int(input('Qual o valor do saque: '))

divid_50 = n1 % 50
divid_20 = divid_50 % 20
divid_10 = divid_20 % 10

if n1 > 0:
    if n1 > 50:
        divid_50_cedula = n1 // 50
        print(f'Você vai receber {divid_50_cedula} cedulas de R$50')
    if divid_50 > 20:
        divid_50 = n1 % 50
        print(f'Você vai receber {divid_50 // 20} cedulas de R$20')
    if divid_20 > 10:
        divid_20 = divid_50 % 20
        print(f'Você vai receber {divid_20 // 10} cedulas de R$10')
    if divid_10 > 1:
        divid_10 = divid_20 % 10
        print(f'Você vai receber {divid_10 // 1} cedulas de R$1')
else:
    print('O despodito tem que ser positivo!')
print('\033[1;33m-=\033[m' * 50)
print('')
