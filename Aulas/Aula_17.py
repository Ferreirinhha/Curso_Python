lista = [1, 3, 5 , 96, 87, 47, 5, 7, 95, 21, 45]
print(f'Lista: {lista} \n')

lista[3] = 9
print(f'Lista mudando o elemento da posição 3 pelo elemento 9: {lista} \n')

lista.append(100)
print(f'Adicionando o elemento 100: {lista} \n')

lista.insert(10, 43)
print(f'Adicionando o elemento 43 na posição 10: {lista} \n')

del lista[5]
print(f'Eliminando o elemento na posição 5 da lista: {lista} \n')

lista.pop()
print(f'Eliminando o último elemento da lista: {lista} \n')

lista.remove(43)
print(f'Eliminando o elemento 43 da lista: {lista} \n')

lista.sort()
print(f'Ordenando a lista: {lista} \n')

lista.sort(reverse=True)
print(f'Invertendo a ordenação: {lista} \n')

for j, i in enumerate(lista):
    print(f'O elemento {i} na posição {j}')

valores = list() # Criando uma nova lista.

for cont in range(0, 5):
    valores.append(int(input('Digite um valor:'))) # Adicionando valores digitados pelo usuário numa lista

a  = [1, 2, 3, 6, 5]

b = a

b[2] = 8 # se fizer assim, mudo o valor do a e do b junto, pq eles formam 1 só

b = a[:] # fiz uma copia dos elementos e passei para o b

b[2] = 8 # agr mudara só do b
