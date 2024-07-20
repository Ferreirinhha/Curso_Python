"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:

1 para binário
2 para octal
3 para hexadecimal
"""

print('')
print('\033[1;33m-=\033[m' * 25)
n1 = int(input('Digite um número: '))
conversao = int(input(""" \nQual será a conversão?

Digite:

\033[36m[1]\033[m para Binário
\033[33m[2]\033[m para Octal
\033[34m[3]\033[m para Hexadecimal

Qual opção: """))

if conversao == 1:
    print(f' \nNúmero convertido para Binário: {bin(n1)[2:]} ')
elif conversao == 2:
    print(f' \nNúmero convertido para Octal: {oct(n1)[2:]}')
elif conversao == 3:
    print(f' \nNúmero convertido para: {hex(n1)[2:]}')
else:
    print('\033[1;4;31mDigite um numero dentre as opções!!!\033[m')
print('\033[1;33m-=\033[m' * 25)
print('') 