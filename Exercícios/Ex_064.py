"""
Crie um programa que leia varios numeros interios pelo teclado. O programa só vai
terminar quando o usuário digitar 999, que é a condição de parada. No final
mostre qquantos números foram digitados e qual foi a soma entre eles.
"""
print('')
print('\033[1;33m-=\033[m' * 30)

cont = 0
parada = 0
while parada < 999:
    if cont < 999:
        n1 = int(input('Digite um número: '))
        cont += 1
    if n1 == 999:
        parada = 999
print(f'{cont - 1} números foram digitados.')
print('Fim.')
print('\033[1;33m-=\033[m' * 30)
print('')