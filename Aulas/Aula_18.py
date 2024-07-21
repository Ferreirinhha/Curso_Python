#Variaveis compostas
#Listas 

lista = list()
pessoas = list()

lista.extend([1, 2, 3]) # Adiciona um inteirável de uma vez na lista
lista.append('Marcos') # Adiciona um único elemento na lista por vez
lista.append(23)
print('Fazendo copias.')
print('')
print(f'Lista: {lista}')

pessoas.append(lista[:])#Fiz uma copia da lista e botei em pessoas
#Se eu não fizer uma copia, quando eu mudar uma lista, vai mudar as duas.
print(f'Pessoas: {pessoas}')

lista[0] = 'Maria'
lista[1] = 18

pessoas.append(lista[:])
print('')
print('Fazendo copias.')
print('')
print(f'Lista: {lista}')
print(f'Pessoas: {pessoas}')

# Sem fazer copias

lista2 = list()
pessoas2 = list()

lista2.append('Joana')
lista2.append(50)

pessoas2.append(lista2)
print('')
print('Sem Fazer copias.')
print('')
print(f'Lista: {lista2}')
print(f'Pessoas: {pessoas2}')

lista2[0] = 'Daniel'
lista[1] = 20
print('')
print('Sem Fazer copias.')
print('')
print(f'Lista: {lista2}')
print(f'Pessoas: {pessoas2}')
