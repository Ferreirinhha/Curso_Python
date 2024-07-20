"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250.00, calcule um aumento de 10%, para inferiores ou iguais
o aumento é de 15%.
"""

salario = float(input('Digite o seu salário: '))

if salario > 1250.00:
    aumento = (salario * 0.10) + salario
    print(f'Você ganhou um aumento de 10%, agora seu salário passou para: {aumento:.2f}')
else:
    aumento = (salario * 0.15) + salario
    print(f'Você ganhou um aumento de 15%, agora seu salário passou para: {aumento:.2f}')