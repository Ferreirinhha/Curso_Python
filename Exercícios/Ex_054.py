"""
Crie um programa que leia a o ano de nascimento de 7 pessoas. No final, diga quantas já atingiram a maior 
idade e quantas não.
"""
import datetime 

print('')
print('\033[1;33m-=\033[m' * 30)

atual = datetime.date.today().year
cont = 0
cont2 = 0

for c in range(1, 8):
    nasc = int(input(f'Que ano a {c}° nasceu: '))

    if atual - nasc >= 18:
        cont += 1
    else:
        cont2 += 1

print(f'{cont} pessoas já atingiram a maior idade e {cont2} ainda não')
print('\033[1;33m-=\033[m' * 30)
print('')