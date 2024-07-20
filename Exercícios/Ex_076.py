"""
Crie um programa que tenha uma tupla única com nome de pordutos e seus respectivos
preços na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

m = 'Mercado Kacedo'
print(f'\033[1;35m{m:=^30}\033[m')

mercado = ('Lubrificante', 10.00, 'Vibrador', 39.99, 'Sugador', 65.90, 'Geo_Sabor', 9.99, 'Langerrie', 49.99)
print('\033[1;33m=\033[m' * 30)
for i in range(0, len(mercado)):
    if i == 0:
        print(f'{mercado[i]:.<20}', end="")
    elif i % 2 == 0:
        print(f'{mercado[i]:.<20}', end="")
    elif i % 2 != 0:
        print(f'R$ {mercado[i]}')
print('\033[1;33m=\033[m' * 30)
    
        