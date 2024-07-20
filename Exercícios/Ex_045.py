#Crie um programa que faça o computador jogar jokenpô com você.
import random
import time

print('')
print('\033[1;33m-=\033[m' * 25)
print('')
print(f'{"JO KEN PO":=^30}')
p1 = int(input("""Escolha:
    [0] Pedra
    [1] Papel
    [2] Tesoura

Qual você escolhe:  """))

escolha = ["Pedra", "Papel", "Tesoura"]
pc = random.randint(0 , 2)

print('')

print('PROCESSANDO...')
time.sleep(1)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')

print('')

if pc == 0: #Jogou pedra
    if p1 == 0:
        print('EMPATE!!!')
    elif p1 == 1:
        print(f'Você GANHOU!!! O pc jogou {escolha[pc]}')
    else:
        print(f'Você PERDEU!!! O pc jogou {escolha[pc]}')
elif pc == 1: #Jogou papel
    if p1 == 0:
        print(f'Você PERDEU!!! O pc jogou {escolha[pc]}')
    elif p1 == 1:
        print('EMPATE!!!')
    else:
        print(f'Você GANHOU!!! O pc jogou {escolha[pc]}')
elif pc == 2: # jogou tesoura
    if p1 == 0:
        print(f'Você GANHOU!!! O pc jogou {escolha[pc]}')
    elif p1 == 1:
        print(f'Você PERDEU!!! O pc jogou {escolha[pc]}')
    else:
        print('EMPATE!!!')
else:
    print('Escolha um número dentre as opções!!!')
print('\033[1;33m-=\033[m' * 25)
print('')

