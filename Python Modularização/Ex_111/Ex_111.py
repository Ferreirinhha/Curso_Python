""" Crie um pacote chamado utilidadesCeV que tenha dois módulos internos 
chamados moeda e dado.

Transfira todas as funções utilizadas nos desafios 107, 108, 109, 110 para o primeiro 
pacote e mantenha tudo funcionando"""

from utilidades_cev import moeda



a = float(input('Digite um valor: '))

print(moeda.aumentar(a, 10, True))