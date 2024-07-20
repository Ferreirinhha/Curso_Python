"""
Faça um programa que leia a altura e a largura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la. 
Sabendo que a cada litro de tinta, pinta uma área de 2m²
"""
altura = float(input('Qual a largura da parede? '))
largura = float(input('Qual a altura? '))

litros_de_tinta = (altura * largura) / 2

print(f'Para pintar uma parede de {altura}x{largura} de dimensão, você precisa de {litros_de_tinta}l de tinta.')