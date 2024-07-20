"""
Aprimore o Desafio 093 para que ele funcione com varíos jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.
"""

dicionario = dict()
adicionar = list()
total_gols = 0

dicionario['Nome'] = str(input('Nome: '))
dicionario['Partidas_Jogadas'] = int(input('Quantas partidas jogadas: '))

for i in range(1, dicionario['Partidas_Jogadas'] + 1):
    gols = int(input(f'Quantos gols na partida {i}: '))
    total_gols += gols 
    adicionar.append(gols)
dicionario['Gols'] = adicionar[:]
dicionario['Total'] = total_gols
print('=-' * 30)
print(dicionario)
print('=-' * 30)

for i, v in dicionario.items():
    print(f'O campo {i} tem o valor: {v}')
print('=-' * 30)
for i in range(0, dicionario['Partidas_Jogadas']):
    if i == 0:
        print(f'O jogador {dicionario['Nome']} jogou {dicionario['Partidas_Jogadas']} partidas.')
    print(f'    => Na partida {i + 1} ele fez {adicionar[i]} gols')
print(f'Foi um total de {total_gols} gols.')

adicionar.clear()