"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em 
um dicionário e todos os dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.
"""

dicionario = dict()
lista = list()
lista_mulheres = list()
media = 0
vezes = int(input('Quantas pessoas serão registradas: '))
for i in range(1, vezes + 1):
    dicionario['Nome'] = str(input('Nome: '))
    dicionario['Idade'] = int(input('Idade: '))
    dicionario['Sexo'] = str(input('Sexo [M/F]: '))
    media += dicionario['Idade']
    if dicionario['Sexo'] in 'Ff':
        lista_mulheres.append(dicionario.copy())
    lista.append(dicionario.copy())

print('Pessoas com a idade acima da média: ')
for i in lista:
    if i['Idade'] > media / vezes:
       for o, v in i.items():
           print(f'{o} = {v}', end=" ")
print(f'Pessoas cadastradas: {vezes}')
print(f'Media idades: {media / vezes}')
print(f'Lista só mulheres: {lista_mulheres}')