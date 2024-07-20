"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km mostre que ele foi multado.

A multa vai custar R$7,00 para cada km ultrapassado
"""

carro = int(input('Digite a velocidade do carro:'))

if carro > 80:
    valor = (carro - 80) * 7
    print(f'Você foi multado! pague sua multa: R${float(valor):.2f}')
    