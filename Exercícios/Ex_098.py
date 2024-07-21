""" Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: inicio, fim e passo e realize a contagem

Seu programa tem que realizar três contagens através da função criada.

A) De 1 até 10, de 1 em 1.

B) de 10 até 0, de 2 em 2.

C) Uma contagem personalizada."""

from time import sleep

def contador(inicio: int, fim: int, passo: int):
    print(f'Contagem de {inicio} a {fim}')
    if passo == 0:
        passo = 1
    if fim == 0:
        fim += -2
    for i in range(inicio, fim + 1, passo):
        print(i, end=" ", flush=True)
    print()

def titulo(text: str):
    tamanho = len(text) + 4
    print('=' * tamanho)
    print(text.center(tamanho))
    print('=' * tamanho)


for i in range(10, -2, -2):
    print(i)

titulo('Contagem')

contador(0, 10, 1)
contador(10, 0, -1)


inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)


