# Dicionários.

dados = dict()
dados2 = { 'nome':'Pedro', 'idade':25}

dados['sexo'] = 'M' # Adicionar elementos

print(dados2['nome']) # Pedro
print(dados2['idade']) # 25

del dados2['idade']

filme = {'titulo':'Star Wars',
         'ano':'1997',
         'diretor': 'George Lucas'
         }
print(filme.values()) # Pegar todos os valores # dict_values(['Star Wars', '1997', 'George Lucas'])
print(filme.keys()) # O nome dos dicionarios # dict_keys(['titulo', 'ano', 'diretor'])
print(filme.items()) # Pega os dois tipo enumerate # dict_items([('titulo', 'Star Wars'), ('ano', '1997'), ('diretor', 'George Lucas')])

for keys,value in filme.items():
    print(f'O {keys} é {value}') #O titulo é Star Wars\  O ano é 1997\ O diretor é George Lucas

locadora = [filme]

print(locadora[0]['ano'])

for i in locadora: # {'titulo': 'Star Wars', 'ano': '1997', 'diretor': 'George Lucas'}
    print(i)

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
brasil.append(estado.copy()) # Não podemos fatiar o dicionario então não da para usar o estado[:]
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')
print(brasil)
print(estado)