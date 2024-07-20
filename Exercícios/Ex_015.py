"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60 por dia e R$0.15 por Km rodado.
"""
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Por quantos Km ele rodou? '))

total = (dias * 60) + (km * 0.15)

input(f'Valor total a ser pago: R${total:.2f}')