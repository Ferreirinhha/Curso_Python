""" Crie um módulo chamado moeda.py que tenha funções incorporadas aumentar()
diminuir(), dobro(), metade().

Faça também um porgrama que importe esse módulo e use algumas dessas funções """

import moeda


moeda1 = float(input('Quanto de dinheiro tem: '))

print(f'Aumentar valor em R$10: {moeda.aumentar(moeda1, 10)}')
print(f'Diminuir valor em R$10: {moeda.diminuir(moeda1, 10)}')
print(f'Metade do valor: {moeda.metade(moeda1)}')
print(f'Dobro do valor: {moeda.dobro(moeda1)}')