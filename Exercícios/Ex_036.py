"""
Escreva um programa para aprovar o empréstimo bancário para comprar uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
será negado.
"""

casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário mensal: '))
anos = int(input('Em quantos anos você que pagar: '))

parcelas = anos * 12
prestacao = casa / (parcelas)
negar = prestacao > salario * 0.3

if negar:
    print('')
    print('\033[1;33mSeu pedido de empréstimo foi \033[4;1;31mNegado!\033[m')
    print('\033[1;33mO valor da pestação excede \033[1;36m30%\033[1;33m do seu salário.')
    print('')
    print(f'Prestação ficaria em: \033[1;31m{parcelas}x de R${prestacao:.2f}\033[m')
    print('')
else:
    print('')
    print('\033[1;33mMeus parabéns, seu pedido de empréstimo foi \033[1;4;32mAprovado!!!')
    print(f'\033[1;4;33mDados:\033[m\n \033[1;4;33mCasa:\033[m R${casa:.2f} \n \033[1;4;33mParecelas:\033[m {parcelas}x de R$ {prestacao:.2f}')
    print('')
