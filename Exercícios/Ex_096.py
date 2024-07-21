"""Faça um programa que tenha uma função chamada área(), que receba as dimensões 
 de um terreno retangular (largura e comprimento) e mostre a área do terreno"""

def area(largura: float, comprimento: float):
    area = largura * comprimento
    print(f'Área to terreno: {area:.2f}')

largura = float(input('Qual a largura do terreno: '))
comprimento = float(input('Qual o comprimento do terreno: '))

area(largura, comprimento)
