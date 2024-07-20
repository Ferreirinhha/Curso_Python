#Faça um programa que leia um ano qualquer e diga se ele é Bixesto.
from datetime import date

ano = int(input('Digite um ano: '))

bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

if ano == 0:
    ano = date.today().year
if bissexto:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
