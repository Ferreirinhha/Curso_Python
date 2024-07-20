"""
Aprimore o desafio anterior mostrando no final.

A) A soma de todos os valores pares digitados.

B) A soma dos valores da terceira coluna.

C) O maior valor da segunda linha.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
linha3 = 0 

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor na posição [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
       

for linha in range(0, 3):
    linha3 += matriz[linha][coluna]
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end=" ")
    print()
print(f'Soma dos números pares: {par}')
print(f'Soma da terceira linha: {linha3}')
print(f'Maior valor terceira linha: {max(matriz[1])}')