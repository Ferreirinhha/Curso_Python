"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do 
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. 
"""

dicionario = dict()
adicionar = list()
total_gols = 0

dicionario['Nome'] = str(input('Nome: '))
dicionario['Partidas_Jogadas'] = int(input('Quantas partidas jogadas: '))

for i in range(1, dicionario['Partidas_Jogadas'] + 1):
    gols = int(input(f'Quantos gols na partida {i}: '))
    total_gols += gols 
    adicionar.append(gols) # Dava para ter adicionado o input dos gols direto no append (seria mais facil)
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