"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato 
Brasileiro de Futebol, na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.

B) Os 4 últimos colocados da tabela.

C) Uma lista com os times em ordem alfabética.

D) Em que posição na tabela está o time da Chapecoense.
"""
print('')
print('\033[1;33m=-\033m' * 30)

brasileirao_times = (
    "Flamengo", "Internacional", "Atlético-MG", "São Paulo", "Fluminense", "Grêmio", 
    "Palmeiras", "Santos", "Athletico-PR", "Corinthians", "Red Bull Bragantino", 
    "Ceará", "Atlético-GO", "Sport", "Bahia", "Fortaleza", "Vasco da Gama", 
    "Goiás", "Coritiba", "Botafogo"
)

print(f'Os cinco primeiros da tabela são:', end=" ")
for i in range(0, 5): # ou da pra fazer assim brasileirao_times[0:5]
    print(f'\033[1;4;{30 + i}m{brasileirao_times[i]}\033[m', end=" ")
    if i == 4:
        print('')

print(f'Os 4 últimos da tabela são:', end=" ")
for i in range(len(brasileirao_times) - 1, len(brasileirao_times) - 5 , -1): # ou da pra fazer assim brasileirao_times[-4:]
    print(f'\033[1;4;{15 + i}m{brasileirao_times[i]}\033[m', end=" ")
print('')

print('Times Organizados por odem Alfabética:')
print(sorted(brasileirao_times), end=" ")

print('')
print(f'Bahia está na posição: {brasileirao_times.index('Bahia')}')

print('\033[1;33m=-\033m' * 30)
print('')