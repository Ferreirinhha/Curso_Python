#Desenvolva um programa que leia o comprimento de 3 retas e diga se elas podem formar um triângulo.

lado1 = float(input('Digite um tamanho para uma reta: '))
lado2 = float(input('Outro: '))
lado3 = float(input('Outro: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Sim, elas podem formar um trinângulo:')
else:
    print('Não, elas não podem formar um triângulo:')