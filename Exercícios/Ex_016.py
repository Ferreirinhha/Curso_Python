#Crie um programa que leia um número real e leia sua porção inteira
#Ex: digite um numero: 6.127
#O número 6.127 tem a porção inteira 6

import math

n1 = float(input('Digite um número: '))
porcao_inteira = math.trunc(n1)

print(f'O número {n1} tem sua porção inteira {porcao_inteira}')