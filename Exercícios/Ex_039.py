"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

Se ele ainda vai se alistar.
Se é a hora de se alistar
Se já passou do alistamento.

Seu programa também deve mostrar o tempo que falta ou que ja passou do prazo.
"""
import datetime

print('')
print('\033[1;33m-=\033[m' * 25)
nasc = int(input('Que ano você nasceu: '))

ano_atual = datetime.date.today().year
idade = ano_atual - nasc
falta = 18 - idade

if idade < 18:
    print(f'Faltam {falta} anos até seu alistamento.')
elif idade > 18:
    print('ja passou da hora de se alistar.')
else:
    print('Ta na hora de se alistar.')
print('\033[1;33m-=\033[m' * 25)
print('')
