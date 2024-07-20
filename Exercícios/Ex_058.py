'''
Melhore o jogo do desafio 28 onde o computador vai 'pensar' em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
'''
from random import randint

print('')
print('\033[1;33m-=\033[m' * 30)
print('')

titulo = 'Jogo da Advinhação'
sortear = randint(0, 10)

print(f'{titulo:=^40} \n')
print('\033[1;36mComputador:\033[m Pensei num número entre 0 e 10!!!\n')

p1 = int(input('Tente adivinhar: '))
cont = 0
print('')

while p1 != sortear:
    print('\033[1;31mErrado HaHa\033[m')
    p1 = int(input('Tente denovo: '))
    print('')
    cont += 1
    if p1 > 10 or p1 < 0:
        print('\033[1;31mBurro!!!\033[m')
        print('Digite um número entre 0 e 10.')
        print('')
        p1 = int(input('Tente denovo: '))
print('\033[1;4;32mAcertou Parabéns!!!\033[m')
print('')
if cont >= 2:
    print(f'\033[1;36mComputador:\033[m Você precisou de \033[1;4;35m{cont + 1} tentativas\033[m para me vencer!')
    print('Que patético!!!')
else:
    print('Parabéns, acertou de primeira. Estou impressionado.')
    print('')
print('Fim.')
print('\033[1;33m-=\033[m' * 30)
print('')



