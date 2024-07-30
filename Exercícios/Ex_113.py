""" Reescreva uma função leiaInt() Que fizemos no fesafio 104, incluindo agora
a possibilidade de digitação de um número de tipo inválido. Aproveite e crie
ambém uma função leiaFloat() com a mesam funcionabilidade. """

""" Crie um programa que tenha a função leiaInt() do Python, só que fazendo a 
validação para aceitar apenas um valor numérico. """

def leia_Int(num: str):
    while True:
        try:
            num = int(input(num))
        except (ValueError):
            print(f'Erro: digite um valor válido!!!')
            continue
        except (KeyboardInterrupt):
            print(f'O usuário preferiu não digitar.')
            return 0
        else:
            return num

def leia_Float(num: str):
    while True:
        try:
            num = float(input(num))
        except:
            print('Erro: digite um valor válido!!!')
            continue
        else:
            return num

n1 = leia_Int('Digite um número: ')
n2 = leia_Float('Digite um número: ')


print(f'O número inteiro digitado foi: {n1} e o float foi {n2}')

