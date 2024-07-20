"""
Crie um programa onde o usuário pode digitar varios valores numéricos e 
cadastre-os em uma lista. Caso o número já exista la dentro, ele não será 
adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
print('')
print('\033[1;33m=-\033m' * 30)
lista = []

while True:
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar[S/N]: ')).upper().strip()
    if num in lista:
        print(f'O elemento \033[1;4;31m{num}\033[m não pode ser adicionado pois já existe na lista.')
    else:
        lista.append(num)
    while continuar != 'S' and continuar != 'N':
         continuar = str(input('Quer continuar[S/N]: ')).upper().strip()
    if continuar[0] == 'N':
        break
lista.sort()
print(f'Lista ordenada: \033[1;32m{lista}\033[m')
print('Fim.')
print('\033[1;33m=-\033[m' * 30)
print('')