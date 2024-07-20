"""
Abrir arquivo: Ctrl + P
Ir para linha: Ctrl + G
Ir para símbolo: Ctrl + Shift + O
Alternar entre arquivos abertos: Ctrl + Tab

Copiar linha (abaixo): Shift + Alt + Down
Copiar linha (acima): Shift + Alt + Up
Mover linha (abaixo): Alt + Down
Mover linha (acima): Alt + Up
Excluir linha: Ctrl + Shift + K
Selecionar linha: Ctrl + L #IMPORTANTE!!!
Comentar em bloco: Shift + Alt + A #IMPORTANTE!!!
Selecionar todas as ocorrências da palavra: Ctrl + Shift + L #IMPORTANTE!!!
Adicionar cursor abaixo: Ctrl + Alt + Down
Adicionar cursor acima: Ctrl + Alt + Up


Buscar e substituir: Ctrl + H #IMPORTANTE!!!
Buscar em arquivos: Ctrl + Shift + F
Buscar e substituir em arquivos: Ctrl + Shift + H
Novo arquivo: Ctrl + N
Abrir arquivo: Ctrl + O
"""

n = int(input())

for i in range(0, n + 1):
    print(i ** 2)

matriz = [
    [1,2,3]
    [4,5,6]
    [7,8,9]
]

len(matriz[0]) # Significa o numero de elementos da primera coluna 
len(matriz[1]) # Significa o numero de elementos da segunda coluna 
len(matriz[2]) # Significa o numero de elementos da terceira coluna 