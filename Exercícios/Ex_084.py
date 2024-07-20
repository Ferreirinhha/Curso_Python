"""
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma
lista. No final mostre.

A) quantas pessoas foram cadastradas.

B) uma listagem com as pessoas mais pesadas.

C)Uma listagem com as pessoas mais leves.
"""
lista = list()
people = list()
plus_weigh = list()
menos_pesadas = list()

while True:
    name = str(input("What's your name: "))
    weigh = float(input("What's your weigh: "))
    cont = str(input('Next [Y/N]: '))

    lista.append(name)
    lista.append(weigh)
    people.append(lista[:])
    lista.clear()

    if weigh >= 100:
        plus_weigh.append(name)
        plus_weigh.append(weigh)
    elif weigh <= 70:
        menos_pesadas.append(name)
        menos_pesadas.append(weigh)

    if cont[0] in 'Nn':
        break
print(f'Lista: {people}')
print(f'Quantas pessoas foram cadastradas: {len(people)}')
print(menos_pesadas)

