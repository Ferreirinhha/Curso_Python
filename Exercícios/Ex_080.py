"""
Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os
em uma lista, já na posição correta de inserção(sem usar o sort())

No final, mostre a lista ordenada na tela.
"""
#Minha resolução pela primeira vez
lista = list()
ind = -1
for i in range(0, 5):
    num = int(input('Digite um número: '))
    lista.append(num)
    ind += 1
    if ind > 0:
        if lista[1] < lista[0]:
            lista.insert(0, num)
            del lista[2]
    if ind > 1:
        if lista[2] < lista[1]:
            lista.insert(1, num)
            del lista[3]
            if lista[1] < lista[0]:
                lista.insert(0, num)
                del lista[2]
    if ind > 2:
        if lista[3] < lista[2]:
            lista.insert(2, num)
            del lista[4]
            if lista[2] < lista[1]:
                lista.insert(1, num)
                del lista[3]
                if lista[1] < lista[0]:
                    lista.insert(0, num)
                    del lista[2]
    if ind > 3:
        if lista[4] < lista[3]:
            lista.insert(3, num)
            del lista[5]
            if lista[3] < lista[2]:
                lista.insert(2, num)
                del lista[4]
                if lista[2] < lista[1]:
                    lista.insert(1, num)
                    del lista[3]
                    if lista[1] < lista[0]:
                        lista.insert(0, num)
                        del lista[2]
print(lista)

#Resolução do professor

lista2 = []

for i in range(0, 5): #Quantidade de vezes que será execultado
    num2 = int(input('Digite um número: '))
    if i == 0 or num2 > lista2[-1]: # se i for igual a primeira posição, add elemento, ou se o num2 for maior que a ultima posição
        lista2.append(num)
    else: 
        pos = 0
        while pos < len(lista2): # vou varrer a lista até 1 antes do último elemento
            if num2 <= lista[pos]: # verificar se o num2 é menor ou igual ao elemento da lista na posição pos
                lista.insert(pos, num2) # se for, inserir o elemento na posição pos
                break
            pos += 1
print(lista2)