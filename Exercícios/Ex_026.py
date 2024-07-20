"""
Faça um programa que leia uma frase pelo teclado e mostre

. Quantas vezes aparece a letra "A"

. Em que posição ela aparece a primeira vez

. Em que posição ela aparece a última vez
"""

frase = str(input('Digite uma frase: ')).strip().upper()

print(f'Quantas letras A: {frase.count('A')}')
print(f'O primeiro A aparece na posição: {frase.find('A')}')
print(f'O útimo A aparece na posição: {frase.rfind('A')}')