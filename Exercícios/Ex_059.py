"""
Crie um programa que leia dois valores e mostre na tela um menu:

[1]somar
[2]multiplicar
[3]maior
[4]novos números 
[5]sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

print('')
print('\033[1;33m-=\033[m' * 30)

menu = 0

while menu != 5:
    if menu == 0 or menu == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print('')
        sleep(1)

    print('\033[1;4;33mO que você quer fazer com os números?\033[m  \n')
    print("""Menu: 
        
    \033[1;32m[1] Somar\033[m
    \033[1;34m[2] Multiplicar\033[m
    \033[1;35m[3] Maior valor\033[m
    \033[1;36m[4] Novos Números\033[m
    \033[1;31m[5] Sair do programa\033[m
    """)
    sleep(1)
    menu = int(input('Qual o opção você quer: '))
    print('')
    if menu == 1:
        print(f'A soma de {n1} + {n2} = {n1 + n2} \n')
        sleep(1)
    elif menu == 2:
        print(f'A multiplicação de {n1} * {n2} = {n1 * n2} \n')
        sleep(1)
    elif menu == 3:
        if n1 < n2:
            print(f'O maior número é o {n2} \n')
            sleep(1)
        else:
            print(f'O maior número é o {n1} \n')
            sleep(1)
print('\033[1;31mFim.\033[m')
print('\033[1;33m-=\033[m' * 30)
print('')
