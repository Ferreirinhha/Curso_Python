"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar. No final mostre:

A) Qual é o total gasto na compra.

B) Quantos produtos custam mais de 1000.

C) Qual é o nome do produto mais barato.
"""
print('')
print('\033[1;33m-=\033[m' * 30)

cont = 0
cont_p = 0
barato = 0
total = 0
nome_produto_barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
    cont += 1
    if cont == 1:
        nome_produto_barato = produto
        barato = preco
    if preco < barato:
        nome_produto_barato = produto
        barato = preco
    if preco > 1000:
        cont_p += 1
    total += preco
    if continuar == 'N':
        break
print(f'O total a pagar será: {total}')
print(f'{cont_p} produtos passaram de R$1000 reais')
print(f'O produto mais barato foi o {nome_produto_barato} custando R${barato:.2f}')
print('\033[1;33m-=\033[m' * 50)
print('')


