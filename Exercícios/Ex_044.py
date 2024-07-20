"""
Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal
e condição de pagamento:

à vista dinheiro/cheque: 10% de desconto

à vista no cartão: 5% de desconto

em até 2x no cartão: preço normal

3x ou mais: 20% juros
"""
print('')
print('\033[1;33m-=\033[m' * 25)

produto = float(input('\n Qual o valor do produto: R$'))
forma_de_pagamento = int(input('\n Digite: \n \n 1 para a pagamento à vista ou cheque: \n 2 para pagamento à vista no cartão: \n 3 para parcelar em até 2x vezes \n 4 para parcelar em 3x ou mais: \n \n Qual será a forma de pagamento: '))

a_vista = produto - (produto * 0.1)
a_vista_cartao = produto - (produto * 0.05)
duas_cartao = produto / 2
juros = produto * 0.2

if forma_de_pagamento == 1:
    print(f'\n Pagando a vista seu produto vai de R${produto:.2f} para R${a_vista:.2f}')
elif forma_de_pagamento == 2:
    print(f'\n Pagando a vista no cartão seu produto vai de R${produto:.2f} para R${a_vista_cartao:.2f}')
elif forma_de_pagamento == 3:
    print(f'\n Pagando em 2x seu produto fica em 2x de R${duas_cartao:.2f}')
elif forma_de_pagamento == 4:
    parcelamento = int(input('\nEm quantas vezes: '))
    if parcelamento > 12 or parcelamento < 1:
        print('\n Você só pode parcelar em até 12X com juros de 20%')
    else:
        tres_ou_mais = (produto + juros) / parcelamento
        print(f'\n Pagando em {parcelamento}x seu produto fica em {parcelamento}x de R${tres_ou_mais:.2f} \n')
else:
    print('\n Escolha um número entre 1 e 4 \n')
print('\033[1;33m-=\033[m' * 25)
print('')