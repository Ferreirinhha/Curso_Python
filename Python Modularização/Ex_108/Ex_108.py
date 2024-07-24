""" Adapte o código do desafio 107, criando uma função adicional chamada moeda
que consiga mostrar os valores como valor monetário formatado """

import moeda


moeda1 = float(input('Digite um valor: '))

print(f'Aumentar valor em R$10: {moeda.moeda2(moeda.aumentar(moeda1, 10))} ')
print(f'Metade do valor: {moeda.moeda2(moeda.metade(moeda1), 'US$')}')
print(f'Diminuir valor: {moeda.moeda2(moeda.diminuir(moeda1, 20))}')