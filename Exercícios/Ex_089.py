"""
Crie um programa que leia o nome e duas notas de varios alunos e guarde tudo em
uma lista composta. No final mostre um boletim contendo a média de cada um e permita
que o usuario possa mostrar as notas de cada aluno individualmente.
"""
print()
print('\033[1;33m=-\033[m' * 30)
notas = list()
armazenar = list()
ver_nota = 0

while True:
    aluno = str(input('Digite o nome do aluno: '))
    armazenar.append(aluno)
    for num_notas in range(1, 3):
        nota = int(input(f'Nota {num_notas}: '))
        armazenar.append(nota)

    continuar = str(input('Quer continuar [S/N]: '))
    notas.append(armazenar[:])
    armazenar.clear()

    if continuar[0] in 'Nn':
        break

print('=' * 30)
for indice, valor in enumerate(notas):
    print(f'Aluno {indice}: {valor[0]:.<20} média: {(valor[1] + valor[2]) / 2}')
print('=' * 30)

while True:
    ver_nota = int(input('Gostaria de ver a nota de qual aluno (somente números) [999 para interromper]: '))
    if ver_nota == 999:
        break
    print(f'Notas: [{notas[ver_nota][1]}] [{notas[ver_nota][2]}]')

print('Fim.')
print('\033[1;33m=-\033[m' * 30)
print()

# Solução professor

ficha = list()
while True:
    aluno = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([aluno, [nota1, nota2], media])
    continuar2 = str(input('Quer continuar [S/N]: '))
    if continuar2 in 'Nn':
        break

for indice, valor in enumerate(ficha):
    print(f'Aluno {indice}: {valor[0]:.<20} média: {valor[2]}')
while True:
    ver = int(input('Quer ver a nota de qual aluno (999 para interromper): '))
    if ver == 999:
        break
    elif ver <= len(ficha) - 1:
        print(f'{ficha[ver][0]}: {ficha[ver][1]}')



