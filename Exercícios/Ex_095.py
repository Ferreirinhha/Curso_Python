"""
Aprimore o Desafio 093 para que ele funcione com varíos jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.
"""

"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do 
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. 
"""

jogador = dict()
time = list()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome Jogador: '))
    jogador['Partidas_jogadas'] = int(input(f'Quantas partidas jogou o {jogador["Nome"]}: '))
    for cont in range(1, jogador['Partidas_jogadas'] + 1):
        partidas.append(int(input(f'Quantos gols na partida {cont}: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total_gols'] = sum(partidas)
    partidas.clear()
    time.append(jogador.copy())
    

    while True:
        continuar = str(input('Quer continuar [S/N]: ')).upper()[0]
        if continuar in 'SN' :
            break 
        else:
            print('Digite S ou N')
    if continuar == 'N':
        break

for i in jogador.keys():
    print(i, end=" ")
for i, v in enumerate(time):
    for d in v.values():
        print(f'\033[1;35md: {str(d)}\033[m', end=" ")
    print()

while True:
    busca = int(input('Qual jogador quer ver od dados (999 interrompe): ')) 
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro')
    else:
        print(f'Levantamento do jogador {time[busca]['Nome']}')
        for i, v in enumerate(time[busca]['Gols']):
            print(f'Na partida {i} fez {v} gols.')
print('Fim!!!')