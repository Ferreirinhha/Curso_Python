# Variaveis compostas (Tuplas) tuplas são IMUTÁVEIS

lanche1 = "hanburguer" # Variáveis simples

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') # Variaveis compostas, () tupla [] Lista {} dicionário

print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(sorted(lanche)) # Mostra o lanche em ordem
print(lanche.index('Suco')) # Que posição está o suco

for c in lanche: #vai percorrer toda a tupla pq lanche é tipo um numero, vai percorrer a quantidade de elementos que ele tem
    print(c)
for c in range(0, len(lanche)):
    print(c)
for c in range(0, len(lanche)):
    print(lanche[c])
for pos, c in enumerate(lanche): # vai pegar a posição com o pos
    print(c, pos)