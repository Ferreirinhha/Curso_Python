"""
Faça um programa que leia 5 valores númericos e guardem numa lista.
No final mostre qual foi o menor e o maior valor em suas respectivas posições.
"""
print('')
print('\033[1;33m=-\033[m' * 30)
lista = list()

for i in range(0, 5):
    lista.append(int(input('Digite um número: ')))
    for j, i in enumerate(lista):
        print(f". + {i}")
        if i == max(lista):
            pos_max = j
        if i == min(lista):
            pos_min = j
# Ou da pra fazer assim...

a = lista.index(max(lista))
b = lista.index(min(lista))

print(lista)
print(f'Menor valor: \033[1;35m{min(lista)}\033[m na posição \033[1;32m{pos_min}\033[m')
print(f'Menor valor: \033[1;35m{max(lista)}\033[m na posição \033[1;32m{pos_max}\033[m')
#Nova forma de fazer...
print(f'Menor valor: \033[1;35m{min(lista)}\033[m na posição \033[1;32m{b}\033[m')
print(f'Menor valor: \033[1;35m{max(lista)}\033[m na posição \033[1;32m{a}\033[m')
print('\033[1;33m=-\033[m' * 30)
print('')

