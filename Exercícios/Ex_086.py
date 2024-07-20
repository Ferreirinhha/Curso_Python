"""
Crie um programa que crie uma matriz de dimensão 3 por 3 e preencha com valores
lidos no teclado.
No final mostre a matriz na tela com a formatação correta.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o um valor na posição [{linha},{coluna}]: '))
print()
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end=" ")
    print()
