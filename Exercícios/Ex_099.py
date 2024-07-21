""" Faça um programa que tenha ma função chamada maior(), que receba vários
parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer quela o deles é o maior."""

from time import sleep

def maior(* num): # alternativa 1
    maior_numero = 0
    for i, v in enumerate(num):
        if i == 0:
            maior_numero = v
        else: 
            if maior_numero < v:
                maior_numero = v
    animation_Analizando()
    print(f'O maior número é o {maior_numero}')

def maior2(* num2): # Alternativa 2 em 1 linha
    print(max(num2))

def animation_Analizando():
    print('Analisando números', end='', flush=True)
    sleep(1)
    print('.', end='', flush=True)
    sleep(1)
    print('.', end='', flush=True)
    sleep(1)
    print('.', end='', flush=True)

maior2(1,2,3,4)
maior2(4,3,2,1)
maior2(5,7,2,9,1,9,0,99)
