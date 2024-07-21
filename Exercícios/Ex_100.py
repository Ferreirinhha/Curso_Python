""" Faça um programa que tenha uma lista chamada números e duas funções chamadas
sortear() e somarPar(). A primeira função vai sortear 5 números e vai colocá-los 
dentro da lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior. """

from random import randint

def sortear(matriz = list):
    matriz.extend([randint(0, 100) for i in range(0, 5)])

def somar_Par(matriz: list):
    soma = 0
    for i in matriz:
        if i % 2 == 0:
            soma += i
    return f'A soma de todos os valores pares: {soma}'


num = list()

sortear(num)

print(f'Lista: {num}')
print(somar_Par(num))


