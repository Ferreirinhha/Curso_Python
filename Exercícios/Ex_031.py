"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens
mais longas. 
"""

Km = float(input('Digite a distância: '))

if Km <= 200:
    valor = 0.50 * Km
    print(f'Valor da viagem: R${valor:.2f}')
elif Km < 0:
    print('Algo está errado, veja se a distância está correta!')
else:
    valor = 0.45 * Km
    print(f'Valor da viagem: R${valor:.2f}')