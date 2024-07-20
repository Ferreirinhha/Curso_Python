"""
Crie um programa que leia varios numeros interios pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o valor maior e menor. O programa
deve perguntar ao usuário se ele quer ou não continuar a digitar.
"""
print('')
print('\033[1;33m-=\033[m' * 30)

cont = 0
continuar = ''
somar = 0
maior = 0
menor = 0

while continuar != 'NAO':
    n1 = int(input('Digite um número: '))
    cont += 1
    somar += n1
    if cont == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        elif n1 < menor:
            menor = n1
    continuar = str(input('Você quer continuar: ')).strip().upper()
print(f'A media dos valores digitados é {somar / cont:.2f}')
print(f'O maior número é o {maior} e o menor é o {menor}')
print('Fim.')
print('\033[1;33m-=\033[m' * 30)
print('')
