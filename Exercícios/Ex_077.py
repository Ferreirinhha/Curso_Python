"""
Crie um programa que tenha uma tupla com várias palavras(não use acentos). Depois 
disso você deve mostrar, para cada palavra, quais são as suas vogais. 
"""
print('')
print('\033[1;33m=-\033m' * 30)

palavras = ('Juana', 'Esquimo', 'Karine', 'Joao', 'Daniel', 'Bobao', 'Cleber', 'Armando')

for i in palavras: # Percorremos cada palavra da tupla
    print('')
    print(f'Na palavra \033[1;4;33m{i}\033[m temos', end=" ")
    for a in i: # Percorremos cada letra de cada palavra
        if a.lower() in 'aeiou': # proucura as vogais da string dentro de cada letra da tupla
            print(f'\033[1;4;35m{a}\033[m', end=" ")
print('\033[1;33m=-\033m' * 30)
print('')