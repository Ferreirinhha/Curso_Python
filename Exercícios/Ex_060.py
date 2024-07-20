# Faça um programa que leia o fatorial de um número.

print('')
print('\033[1;33m-=\033[m' * 30)

n1 = int(input('Digite um número: '))
print('')

cont = 0
fatorial = n1

print(f'O fatorial de {n1}! é ', end="")
while cont < n1:
    if cont == 0:
        print(n1, end="")
        cont += 1
    fatorial *= cont
    print(f' * {n1 - cont}', end="")
    cont += 1
print(f' = {fatorial}')
print('\033[1;33m-=\033[m' * 30)
print('')

    
   