"""
Crie um programa que leia uma frase e diga se ela é ou não palindroma, desconsiderando os espaços.
"""

print('')
print('\033[33m-=\033[m' * 20)

f1 = str(input('Digite uma frase: ')).strip().upper()

separar = f1.split() # separa
juntar = ''.join(separar) # junta a frase
reverso = ''

reverso2 = juntar[::-1] # le ao contrario
print(reverso2)

for c in range(len(juntar) - 1, -1, -1): # le a frase do inverso, pegando a posição final da ultima letra e indo de tras pra frente
    reverso += juntar[c] # adiciona a frase no inverso em 'reverso'

if reverso == juntar: # verifica se o reverso é igual a juntar, precisa ser fora pq estamos verificando a frase final e não cada letra
    print(f'A frase {f1} é palindroma. {juntar} e {reverso}')
else:
    print(f'A frase {f1} não é palindroma. {juntar} e {reverso}')
print('\033[33m-=\033[m' * 20)
print('')