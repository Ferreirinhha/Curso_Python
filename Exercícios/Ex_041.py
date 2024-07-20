"""
A Confederação Nacional de Natação precisa de um programa que leia o ano
 de nascimento de um attleta e mostre a sua categoria, de acordo com a idade:

 Até 9 anos: Mirim
 Até 14 anos: Infantil
 até 19 anos: Junior
 até 25 anos: Sênior
 Acima: Master
"""
from datetime import date

print('')
print('\033[1;33m-=\033[m' * 25)

ano_autal = date.today().year

nasc = int(input('Que ano você nasceu: '))
idade = ano_autal - nasc

print(f'Atleta tem {idade} e é considerado: ')
if idade <= 9:
    print('\033[1;4;36mMirim\033[m')
elif idade > 9 and idade <= 14:
    print('\033[1;4;36mInfantil\033[m')
elif idade > 14 and idade <= 19:
    print('\033[1;4;36mJunior\033[m')
elif idade > 19 and idade <= 25:
    print('\033[1;4;36mSênior\033[m')
else:
    print('\033[m1;4;36mMaster\033[m')
print('\033[1;33m-=\033[m' * 25)
print('')