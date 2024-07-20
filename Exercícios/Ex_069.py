"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não
coninuar. No final mostre:

A) Quantas pessoas tem mais de 18 anos.

B) Quantos homens foram cadastrados.

C) Quantas mulheres tem menos de 20 anos.
"""
print('')
print('\033[1;33m-=\033[m' * 30)

cont_P = 0
cont_I = 0
cont_M = 0
cont_F = 0

while True:
    cont_P += 1
    idade = int(input(f'Qual a idade da {cont_P}° pessoa: '))
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input(f'Qual o sexo da {cont_P}° pessoa [M/F]: ')).strip().upper()[0]
    continuar = str(input('Quer continuar [S/N]:')).strip().upper()

    if idade > 18:
        cont_I += 1
    if sexo == 'M':
        cont_M += 1
    if sexo == 'F' and idade < 20:
        cont_F
    if continuar == 'N':
        break

print(f'Número de pessoas com mais de 18 anos: {cont_I}')
print(f'Número de Homens cadastrados: {cont_M}')
print(f'Número de Mulheres com menos de 20 anos: {cont_F}')
print('\033[1;33m-=\033[m' * 50)
print('')
