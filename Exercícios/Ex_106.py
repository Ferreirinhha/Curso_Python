""" Faça um mini-sistema que utilize o interactive Help do Pyhton. O usuário vai
digitar o comando e o manual vai aparecer. Quando o usuário digitar 'FIM', o
programa se encerrará.  """

#Falta pintar

while True:
    nome = str(input('Input: ')).lower().strip()
    if nome == 'fim':
        break
    else:
        help(nome)