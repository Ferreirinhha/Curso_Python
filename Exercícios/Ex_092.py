"""
Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
dicionário se por acaso o CTPS for diferente de 0, o dicionário receberá tabmbém o ano de contratação
e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
import datetime

ano_atual = datetime.date.today().year

dicionario = dict()
while True:
    dicionario['Nome'] = str(input('Nome: '))
    nascimento = int(input('Ano de nascimento: '))
    dicionario['Carteira'] = int(input('Carteira de trabalho (0 se não tiver): '))
    dicionario['Idade'] = ano_atual - nascimento
    if dicionario['Carteira'] == 0:
        break
    dicionario['Ano_Contratado'] = int(input('Ano que foi contratado: '))
    dicionario['Salário'] = float(input('Qual o salário: '))
    dicionario['Aposentadoria'] =  ((dicionario['Ano_Contratado'] + 35) - ano_atual) + dicionario['Idade']
    break
for indice, valor in dicionario.items():
    if indice == 'Idade':
        print(f'A {indice} é: {valor}')
    elif indice == 'Aposentadoria':
        print(f'A {indice} é com: {valor} anos')
    else:
        print(f'O {indice} é: {valor}')