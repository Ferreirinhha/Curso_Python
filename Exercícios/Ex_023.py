"""
Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separeados

unidade,dezena,centena,milhar
"""

n1 = int(input('Digite um número: '))

print(f'Analisando o numero {n1}')
print(f'Unidades: {n1 // 1 % 10}')
print(f'Dezena: {n1 // 10 % 10}')
print(f'Centena: {n1 // 100 % 10}')
print(f'Milhar: {n1 // 1000 % 10}')