def aumentar(preco=0, botar=0, conv=False): 
    if conv:
        return moeda2(preco)
    else:
        return preco + botar


def diminuir(preco=0, tirar=0, conv=False): 
    if conv:
        return moeda2(preco)
    else:
        return preco - tirar


def dobro(preco=0, conv=False):
    if conv:
        return moeda2(preco)
    else:
        return preco * 2
    
    
def metade(preco=0, conv=False):
    if conv:
        return moeda2(preco)
    else:
        return preco / 2


def moeda2(preco=0, conv='R$'):
    return f'{conv}{preco:.2f}'

