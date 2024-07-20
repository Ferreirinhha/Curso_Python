"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
calcule e mostre o comprimento da hipotenusa
"""
from math import sqrt, hypot

cateto_oposto = float(input('Qual o cateto oposto: '))
cateto_adjacente = float(input('Qual o Adjacente: '))
hipotenusa = sqrt((cateto_adjacente * cateto_adjacente) + (cateto_oposto * cateto_oposto))

print('_' * 20)
print('Com calculo matemático normal:')
print(f'Calculando o valor do cateto adjacente {cateto_adjacente} e do cateto oposto {cateto_oposto} \n temos o hipotenusa {hipotenusa:.2f}')
print('_' * 20)

hipotenusa2 = hypot(cateto_adjacente,cateto_oposto)

print('Usando o Math: ')
print(f'Calculando o valor do cateto adjacente {cateto_adjacente} e do cateto oposto {cateto_oposto} \n temos o hipotenusa {hipotenusa2:.2f}')