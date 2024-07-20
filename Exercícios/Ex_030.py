#Crie um programa que diga se o número é par ou impar

n1 = int(input('Digite um número: '))

if n1 % 2 == 0:
    print(f'O número {n1} é PAR.')
else:
    print(f'O número {n1} é ÍMPAR')