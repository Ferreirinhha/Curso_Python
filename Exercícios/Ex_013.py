#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Qual o seu salário? R$'))
aumento = salario + (salario * 0.15)

print(f'Meus parabéns, você ganhou 15% de aumento, seu salário de R${salario} vai para R${aumento:.2f}')
