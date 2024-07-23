""" Crie um programa que tenha a função leiaInt() do Python, só que fazendo a 
validação para aceitar apenas um valor numérico. """

def leia_int(num: str):
    while True:
        if num.isnumeric() == True:
            break
        else:
            num = input(str('\033[1;31mErro: Por favor digite um número: \033[m'))
    return f'Número digitado: {num}'


numero = input(str('Digite um número: '))

resp = leia_int(numero)
print(resp)