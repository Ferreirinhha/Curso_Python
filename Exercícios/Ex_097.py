""" Faça um programa que tenha uma função chamada escreva(), que receba um
texto qualquer como parâmetro e mostre uma mensagem com o tamanho adaptável """

def escrever(frase: str):
    tamanho = len(frase)
    print('~' * tamanho, end="~~~~")
    print(f'\n  {frase}')
    print('~' * tamanho, end="~~~~")

escrever('Macedo')

