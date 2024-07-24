""" Crie um módulo chamado moeda.py que tenha funções incorporadas aumentar()
diminuir(), dobro(), metade().

Faça também um porgrama que importe esse módulo e use algumas dessas funções """

def aumentar(preco=0, botar=0, conv=False): # Resultado do ex109
    if conv:
        return moeda2(preco)
    else:
        return preco + botar


def diminuir(preco=0, tirar=0): # Resultado do EX 107
    return preco - tirar


def dobro(preco=0):
    return preco * 2
    
    
def metade(preco=0):
    return preco / 2


def moeda2(preco=0, conv='R$'): # Resultado do ex 108
    return f'{conv}{preco:.2f}'


def titulo(palavra = ''):
    tam = len(palavra) * 4
    print('~' * tam)
    print(palavra.center(tam))
    print('~' * tam)


def resumo(palavra, preco, botar, tirar):
    titulo(palavra)
    print(f'Aumento de R${botar}: {moeda2(aumentar(preco, botar))}')
    print(f'Diminuir em R$10: {diminuir(preco, tirar)}')
    print(f'Metade do preco: {metade(preco)}')
    print(f'Dobro do preco: {dobro(preco)}')
    print('~' * 40)
