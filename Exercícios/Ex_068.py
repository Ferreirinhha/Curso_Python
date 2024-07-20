"""
Faça um programa que jogue par ou Ímpar com o computador, O jogo só será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final
do jogo.
"""
import random

cont = 0
titulo = 'PAR OU ÍMPAR'

print('')
print(f'\033[1;33m{titulo:=^50}\033[m')
print('')

while True:
    n1 = int(input('Qual número você vai jogar: '))
    p1 = str(input('\033[1;34mPAR\033[m \033[1;33mou\033[m \033[1;36mÍMPAR\033[m \033[1;33m( [\033[m\033[1;34mP\033[m/\033[1;36mI\033[m\033[1;33m] ): \033[m')).strip().upper()
    print('')
    pc = random.randint(0, 10)
    par = (n1 + pc) % 2 == 0
    impar = (n1 + pc) % 2 != 0

    if p1 == 'P': # Jogou Par
        if par:
            print('\033[1;4;32mVocê Ganhou!\033[m')
            print(f'O pc jogou \033[1;4;35m{pc}\033[m e você jogou \033[1;4;33m{n1}\033[m o resultado é \033[1;4;34mPAR\033[m')
            print('')
            cont += 1
        else:
            print('\033[1;4;31mVocê Perdeu!\033[m')
            print(f'O pc jogou \033[1;4;35m{pc}\033[m e você jogou \033[1;4;33m{n1}\033[m o resultado é \033[1;4;36mÍMPAR\033[m')
            print('')
            break
    elif p1 == 'I': # Jogou ímpar
        if impar:
            print('\033[1;4;32mVocê Ganhou!\033[m')
            print(f'O pc jogou \033[1;4;35m{pc}\033[m e você jogou \033[1;4;33m{n1}\033[m o resultado é \033[1;4;36mÍMPAR\033[m')
            print('')
            cont += 1
        else:
            print('\033[1;4;31mVocê Perdeu!\033[m')
            print(f'O pc jogou \033[1;4;35m{pc}\033[m e você jogou \033[1;4;33m{n1}\033[m o resultado é \033[1;4;34mPAR\033[m')
            print('')
            break
    else:
        print('\033[1;4;31mOpção inválida!\033[m')
        print('')
print(f'Você ganhou \033[1;4;32m{cont}\033[m consecutivas!!!')
print('\033[1;33m-=\033[m' * 50)
print('')