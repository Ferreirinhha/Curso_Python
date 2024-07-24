""" Crie um módulo chamado moeda.py que tenha funções incorporadas aumentar()
diminuir(), dobro(), metade().

Faça também um porgrama que importe esse módulo e use algumas dessas funções """

def aumentar(preco=0, botar=0, conv=False):
        return preco + botar


def diminuir(preco=0, tirar=0):
    return preco - tirar


def dobro(preco=0):
    return preco * 2
    
    
def metade(preco=0):
    return preco / 2


def moeda2(preco=0, conv='R$'):
    return f'{conv}{preco:.2f}'