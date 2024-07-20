"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome 
separadamente.
"""

nome = input('Digite seu nome completo: ').strip()
dividir = nome.split()

print(f'Primeiro nome: {dividir[0]} ')
print(f'Último nome: {dividir[(len(dividir) - 1)]}')