""" Faça um progama que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota 
- A média da turma
- A situação (Opcional) 

Coloque também DOCSTRINGS """


def notas(* notas, situacao=False):
    """ 
    notas: Notas dos alunos
    situação: Booleano  
    """
    dicionario = {'Maior nota': max(notas), 'Menor nota': min(notas)}
    cont = 0
    for i in notas:
        cont += 1
    dicionario['Total notas'] = cont
    dicionario['Média turma'] = sum(notas) / cont
    if situacao == True:
        if dicionario['Média turma'] < 6:
            dicionario['Situação'] = 'Reprovado'
        else:
            dicionario['Situação'] = 'Aprovado'
    return dicionario

result = notas(10,6,5,2,9,8, situacao=True)
print(result)

help(notas)
