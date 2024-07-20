"""
Crie um programa que leia o nome completo de uma pessoa e mostre

. O nome com todas as letras em maiúsculas

. O nome com todas minúsculas

. Quantas letras ao todo(Sem considerar os spaços)

. Quantas letras tem o primeiro nome
"""

nome = input('Qual o seu nome? ').strip()
dividido = nome.split()

print(f'Maiúsculo: {nome.upper()}')
print(f'Minúsculo: {nome.lower()}')
print(f'Tamanho sem espaços: {len(nome) - nome.count(' ')} ')
print(f'Tamanho primeiro nome: {len(dividido[0])}')