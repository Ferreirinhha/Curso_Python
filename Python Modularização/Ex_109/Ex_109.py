""" Modifique as funções que foram criadas no desafio 107 para que elas aceitem
um parâmetro a mais, informando se o valor ratornado por elas vai ser ou não 
formatado pela função moeda(), desenvolvida no desafio 108. """


import moeda


moeda1 = float(input('Digite um valor: '))


print(f'Valor aumentado em R$10:{moeda.aumentar(moeda1, 10, conv=True):.>20}')
print(f'Valor diminuido em R$10:{moeda.diminuir(moeda1, 10, True):.>20}')
print(f'Dinheiro pela metade:{moeda.metade(moeda1, True):.>20}')
print(f'Dobro do dinheiro:{moeda.dobro(moeda1, True):.>20}')