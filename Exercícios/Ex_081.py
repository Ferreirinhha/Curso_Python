"""
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados.

B) A lista de valores ordenados de forma decrescente.

C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = list()
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
    while continuar[0] != 'S' and continuar[0] != 'N': # um tem que ser falso para sair ou para não entrar
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
lista.sort(reverse=True)
print(f'Números digitados: {len(lista)} ')
print(f'Valores ordenados de forma decrescente: {lista} ')
if 5 in lista:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')
print('Fim.')