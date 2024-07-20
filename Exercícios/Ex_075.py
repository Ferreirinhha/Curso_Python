"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
tupla. No final mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi difitado o primerio 3.

C) Quais foram os números pares.
"""
print('')
print('\033[1;33m=-\033m' * 30)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite só mais um número: '))

tupla = (n1, n2, n3, n4)

print('\033[1;33m=-\033m' * 30)

print(f'Tupla: {tupla}')
print(f'O número 9 apareceu: {tupla.count(9)} vezes')

if 3 not in tupla:
    print('O número 3 não foi encontrado')
else:
    print(f'A posição do primeiro 3 foi: {tupla.index(3)}')
print('Números pares: ', end="")
for c in tupla:
    if c % 2 == 0:
        print(c, end=" ")
print('')
print('\033[1;33m=-\033m' * 30)
print('')               

