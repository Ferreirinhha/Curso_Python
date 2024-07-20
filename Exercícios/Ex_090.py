"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

aluno = dict()

aluno['Nome'] = str(input('Digite o nome do aluno: '))
while True:
    aluno['Média'] = float(input('Digite a média do aluno: '))
    print()
    if 6 <= aluno['Média'] < 10:
        aluno['Situação'] = 'APROVADO!!!'
        break
    elif 0 <= aluno['Média'] < 6:
        aluno['Situação'] = 'REPROVADO!!!'
        break
    else:
        print('Digite uma nota maior que 0 ou menor que 10.')
print('=-' * 20)
for i, v in aluno.items():
    print(f'{i} do aluno(a) é \033[1;4;35m{v}\033[m')
    print()

print(aluno)
print('=-' * 20)
