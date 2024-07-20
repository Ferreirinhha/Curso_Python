"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, 
de acordo com a média atiginda:

Abaixo de 5.0: Reprovado

Entre 5.0 e 6.9: Recuperação

Superior ou igual a 7.0: Aprovado
"""
print('')
print('\033[1;33m-=\033[m' * 25)

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(' \nAluno ficou \033[1;4;31mReprovado.\033[m')
elif media >= 5 and media <= 6.9:
    print(' \nAluno ficou de \033[1;4;33mRecuperação.\033[m')
else:
    print(' \nAluno foi \033[1;4;32mAprovado.\033[m')
print('\033[1;33m-=\033[m' * 25)
print('')