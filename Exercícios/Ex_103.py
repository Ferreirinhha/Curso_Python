""" Faça um programa que tenha uma função chamada ficha(), que receba dois
parâmetros opicionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que tenha algum
dado não tenha sido informado corretamente. """

def ficha(nome="", gols='0'):
    jogador = {"Nome": nome, "Gols": gols}
    for i,v in jogador.items():
        if nome == "":
            return f"O jogador <desconhecido> fez {jogador['Gols']} gols na sua carreira"
        else:
            return f"O jogador {jogador['Nome']} fez {jogador['Gols']} gols na sua carreira"

jogador = str(input('Nome do jogador: '))
gols = str(input('Quantos gols feitos: '))

result = ficha(jogador, gols)

print(result)
