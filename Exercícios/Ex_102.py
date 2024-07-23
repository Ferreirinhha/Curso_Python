""" Crie um programa que tenha uma função fatorial() que receba dois parâmetros
o primeiro que indique o número a calcular e o outro chamado show, que receberá
um valor lógico(opicional) indicando se será mostrado ou não na tela o processo 
de cálculo do fatorial. """

def fatorial(num: int, show=False):
    for i in range(num - 1, 0, -1):
        if show:
            num *= i
            if i > 1:
                print(f'{i} x', end=" ")
            elif i <= 1:
                print(f'{i} =', end=" ")
        else:
            num *= i
    return num

resultado = fatorial(10, show=True)
print(f'Resultado fatorial: {resultado}')
