"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por 
extenso, de zero a vinte.

Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostrálo por extenso
"""
print('')
print('\033[1;33m=-\033m' * 30)
n = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
    'dezoito', 'dezenove', 'vinte'
    )
n1 = int(input('Digite um número: '))

print(f'O número digitado foi o {n[n1]}')
print('\033[1;33m=-\033m' * 30)
print('')