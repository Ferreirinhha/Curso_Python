#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média

aluno = input('Qual o nome do Aluno? ')
nota1 = float(input('Qual a nota do primeiro período? '))
nota2 = float(input('Qual a nota do segundo período? '))

media = (nota1 + nota2) / 2

if (media >  6.0):
    print(f'O aluno {aluno} no primeiro período em História tirou {nota1} \n No segundo período tirou {nota2} \n sua média ficou com: {media:.2f} e ficou APROVADO')
else:
    print(f'O aluno {aluno} no primeiro período em História tirou {nota1} \n No segundo período tirou {nota2} \n sua média ficou com: {media:.2f} e ficou REPROVADO')