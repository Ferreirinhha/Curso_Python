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
    dicionario['Total notas'] = len(notas)
    dicionario['Média turma'] = sum(notas) / len(notas)
    if situacao:
        if dicionario['Média turma'] < 6:
            dicionario['Situação'] = 'Reprovado'
        else:
            dicionario['Situação'] = 'Aprovado'
    return dicionario

result = notas(10,6,5,2,9,8, situacao=True)
print(result)

help(notas)
