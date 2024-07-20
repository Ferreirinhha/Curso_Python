"""
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
"""

lista = []
lista_par = []
lista_impar = []
cont = 0

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont += 1
    if cont == 10:
        break
for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print(f'Lista: {lista}')
print(f'Lista par: {lista_par}')
print(f'Lista ímpar: {lista_impar}')
print('Fim.')